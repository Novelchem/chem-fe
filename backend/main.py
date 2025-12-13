from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import User,History
from passlib.context import CryptContext
from model import run_with_manual_orchestration
from auth import router as auth_router
from database import get_db
from typing import Dict, Any, List

app = FastAPI()
app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    user_id: int
    pic50_min: float
    pic50_max: float
    atom_min: float
    atom_max: float
    logP_min: float
    logP_max: float



@app.post("/predict")
def predict(data: InputData) -> Dict[str, Any]:
    """
    Menjalankan Agentic AI pipeline (generate, validate, justify, image)
    dan mengembalikan hasil yang siap ditampilkan di frontend.
    """
    try:
        # 1. FORMAT INPUT: Mengubah 6 variabel min/max menjadi 1 string constraints
        # Constraint string harus sesuai format yang diharapkan oleh parse_constraints di model_agent.py
        constraints_text = f"""
        pIC50: {data.pic50_min}-{data.pic50_max}
        logP: {data.logP_min}-{data.logP_max}
        atoms: {int(data.atom_min)}-{int(data.atom_max)}
        """
        
        print("Constraints Dibuat:", constraints_text.strip())

        # 2. MENJALANKAN AGENTIC ORCHESTRATION DARI TIM ML
        # run_with_manual_orchestration mengembalikan dict dengan key 'results', 'constraints', dll.
        raw_agent_output = run_with_manual_orchestration(
            constraints=constraints_text
        )

        # Cek jika ada error dari Agent
        if "error" in raw_agent_output:
             raise Exception(f"Agent Error: {raw_agent_output['error']}")

        print("RAW AGENT OUTPUT:", raw_agent_output)

        # 3. NORMALISASI OUTPUT: Mengubah format Agent ke format yang diharapkan Vue.js
        results_for_frontend: List[Dict[str, Any]] = []
        
        # Iterasi hanya pada molekul yang berhasil dibuat dan divalidasi
        for item in raw_agent_output.get("results", []):
            
            # Kita hanya mengirim molekul yang 'valid' dan punya 'image_base64'
            if item.get("valid") and item.get("image_base64"):
                
                props = item.get("properties", {})
                
                results_for_frontend.append({
                    "smiles": item.get("smiles"),
                    "justification": item.get("justification", "No scientific justification available."),
                    # Mengambil image_base64 dari Agent. 
                    # Kita asumsikan frontend yang menambahkan prefix 'data:image/png;base64,'
                    "image": item.get("image_base64"), 
                    
                    # Properti Disesuaikan dengan key yang digunakan di detail.vue (pIC50, logP, atom_count)
                    "properties": {
                        "pIC50": props.get("pIC50"), # pIC50 (Camel Case)
                        "logP": props.get("logP"), # logP
                        "atom_count": props.get("atoms"), # atoms -> atom_count
                    }
                })

        return {
            "success": True,
            "results": results_for_frontend, # Kirim list of final, valid molecules
            "count": len(results_for_frontend),
        }

    except Exception as e:
        # Jika terjadi error saat parsing, koneksi LLM, atau error lainnya
        print(f"SERVER ERROR: {e}")
        return {
            "success": False,
            "error": f"Gagal memproses permintaan: {str(e)}",
            "results": []
        }



@app.get("/health")
def health_check():
    return {"status": "ok"}

# ===========================
# HISTORY GET
# ===========================
@app.get("/history/user/{users_id}")
def get_user_history(users_id: int, db: Session = Depends(get_db)):
    histories = (
        db.query(History)
        .filter(History.user_id == users_id)
        .order_by(History.id.desc())
        .all()
    )

    return {
        "success": True,
        "history": [
            {
                "id": h.id,
                "user_id": h.user_id,
                "smiles": h.smiles,
                "pLC50": getattr(h, "pLC50", None),  # DB pLC50 -> frontend pLC50
                "atom_count": h.atom_count,
                "logP": h.logP,
                "justification": getattr(h, "justification", None)
            }
            for h in histories
        ]
    }

# ===========================
# HISTORY POST / ADD
# ===========================
@app.post("/history/add")
def add_history(item: dict, db: Session = Depends(get_db)):
    history_entry = History(
        user_id=item["user_id"],          
        pLC50=item.get("pIC50"),          # frontend pIC50 -> DB pLC50
        atom_count=item.get("atom_count"),
        logP=item.get("logP"),
        smiles=item.get("smiles"),
        justification=item.get("justification")
    )

    db.add(history_entry)
    db.commit()
    db.refresh(history_entry)

    return {
        "success": True,
        "message": "History saved",
        "data": {
            "id": history_entry.id,
            "user_id": history_entry.user_id,
            "smiles": history_entry.smiles,
            "pLC50": history_entry.pLC50,
            "atom_count": history_entry.atom_count,
            "logP": history_entry.logP,
            "justification": history_entry.justification
        }
    }
