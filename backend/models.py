# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # Base dari database.py

class User(Base):
    __tablename__ = "users"  # nama tabel di database

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)

    # Relasi ke tabel History
    histories = relationship("History", back_populates="owner")


# ---- Tambahan baru untuk history ----
class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Field harus sesuai dengan main.py
    pLC50 = Column(String(50))
    atom_count = Column(String(50))
    smiles = Column(String(255))
    logP = Column(String(50))
    justification = Column(String(255))  # Supaya bisa simpan justification dari model

    owner = relationship("User", back_populates="histories")