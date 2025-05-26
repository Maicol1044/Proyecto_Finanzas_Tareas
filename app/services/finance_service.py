# app/services/finance_service.py
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models.finance import Finance, TransactionType
from ..schemas.finance import FinanceCreate, FinanceUpdate

def get_finances(db: Session):
    return db.query(Finance).order_by(Finance.date.desc()).all() # Updated column name

def get_finance(db: Session, finance_id: int):
    return db.query(Finance).filter(Finance.id == finance_id).first()

def create_finance(db: Session, finance: FinanceCreate):
    db_finance = Finance(
        type=finance.type, # Updated field name
        amount=finance.amount, # Updated field name
        category=finance.category, # Updated field name
        date=finance.date # Updated field name
    )
    db.add(db_finance)
    db.commit()
    db.refresh(db_finance)
    return db_finance

def update_finance(db: Session, finance_id: int, finance: FinanceUpdate):
    db_finance = db.query(Finance).filter(Finance.id == finance_id).first()
    if db_finance:
        db_finance.type = finance.type       # Updated field name
        db_finance.amount = finance.amount   # Updated field name
        db_finance.category = finance.category # Updated field name
        db_finance.date = finance.date       # Updated field name
        db.commit()
        db.refresh(db_finance)
    return db_finance

def delete_finance(db: Session, finance_id: int):
    db_finance = db.query(Finance).filter(Finance.id == finance_id).first()
    if db_finance:
        db.delete(db_finance)
        db.commit()
    return db_finance

def get_financial_summary(db: Session):
    total_income = db.query(func.sum(Finance.amount)).filter(Finance.type == TransactionType.income).scalar() or 0 # Updated column name and enum
    total_expenses = db.query(func.sum(Finance.amount)).filter(Finance.type == TransactionType.expense).scalar() or 0 # Updated column name and enum
    balance = total_income - total_expenses

    return {
        "total_income": total_income,   # Updated key
        "total_expenses": total_expenses, # Updated key
        "balance": balance,
    }

