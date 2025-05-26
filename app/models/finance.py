# app/models/finance.py
from sqlalchemy import Column, Integer, String, Float, Date, Enum
import enum
from ..database import Base

class TransactionType(str, enum.Enum):
    income = "income" # Changed to English
    expense = "expense" # Changed to English

class Finance(Base):
    __tablename__ = "finances"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(TransactionType), nullable=False) # Changed column name
    amount = Column(Float, nullable=False) # Changed column name
    category = Column(String, nullable=False) # Changed column name
    date = Column(Date, nullable=False) # Changed column name


