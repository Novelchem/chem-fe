# auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from passlib.context import CryptContext
from pydantic import BaseModel

router = APIRouter()

# =========================
# Password hashing context
# =========================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
MAX_PASSWORD_LEN = 72  # Bcrypt limit

# =========================
# Pydantic schema
# =========================
class UserSchema(BaseModel):
    username: str
    email: str
    password: str

class LoginSchema(BaseModel):
    email: str
    password: str

# =========================
# Database dependency
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# Register endpoint
# =========================
@router.post("/register")
def register(user: UserSchema, db: Session = Depends(get_db)):
    # Cek email sudah terdaftar
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Batasi panjang password
    safe_password = user.password[:MAX_PASSWORD_LEN]
    hashed_password = pwd_context.hash(safe_password)

    # Simpan user baru
    new_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

# =========================
# Login endpoint
# =========================
@router.post("/login")
def login(user: LoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Return id, username, email supaya frontend bisa simpan user_id untuk history
    return {
        "message": "Login successful",
        "user": {
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email
        }
    }
