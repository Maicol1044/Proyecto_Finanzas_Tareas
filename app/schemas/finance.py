# app/schemas/finance.py
from pydantic import BaseModel, ConfigDict
from datetime import date
import enum

class TransactionType(str, enum.Enum): 
    income = "income"
    expense = "expense"

class FinanceBase(BaseModel):
    type: TransactionType  
    amount: float            
    category: str           
    date: date               

class FinanceCreate(FinanceBase):
    pass

class FinanceUpdate(FinanceBase):
    pass

class FinanceOut(FinanceBase):
    id: int
    model_config = ConfigDict(from_attributes=True)