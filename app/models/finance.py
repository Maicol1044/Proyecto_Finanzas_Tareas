# app/models/finance.py
from sqlalchemy import Column, Integer, String, Float, Date, Enum
import enum
from ..database import Base

class TransactionType(str, enum.Enum):
    income = "income" 
    expense = "expense" 

class Finance(Base):
    __tablename__ = "finances"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(TransactionType), nullable=False) 
    amount = Column(Float, nullable=False) 
    category = Column(String, nullable=False) 
    date = Column(Date, nullable=False) 


