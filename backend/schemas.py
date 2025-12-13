# schemas.py
from pydantic import BaseModel

# Schema untuk membuat history baru
class HistoryCreate(BaseModel):
    pic50: str
    atom_count: str
    logp: str

# Schema untuk response history
class HistoryResponse(BaseModel):
    id: int
    pic50: str
    atom_count: str
    logp: str

    class Config:
        orm_mode = True
