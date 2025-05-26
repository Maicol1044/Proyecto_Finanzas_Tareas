# app/schemas/finance.py
from pydantic import BaseModel, ConfigDict
from datetime import date
import enum

class TransactionType(str, enum.Enum): # Must match model enum
    income = "income"
    expense = "expense"

class FinanceBase(BaseModel):
    type: TransactionType    # Changed field name
    amount: float            # Changed field name
    category: str            # Changed field name
    date: date               # Changed field name

class FinanceCreate(FinanceBase):
    pass

class FinanceUpdate(FinanceBase):
    pass

class FinanceOut(FinanceBase):
    id: int
    model_config = ConfigDict(from_attributes=True)