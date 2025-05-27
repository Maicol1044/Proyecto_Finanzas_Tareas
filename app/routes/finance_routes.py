from itertools import count
from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.status import HTTP_303_SEE_OTHER
from datetime import date
from collections import defaultdict

from app.config import templates

from ..database import get_db
from ..services import finance_service
from ..schemas import finance as schemas
from ..models import finance as models

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def read_finances(request: Request, db: Session = Depends(get_db)):
    finances = finance_service.get_finances(db)
    summary = finance_service.get_financial_summary(db)

    expenses_by_category = defaultdict(float)
    income_by_category = defaultdict(float)

    for f in finances:
        if f.type == models.TransactionType.expense:
            expenses_by_category[f.category] += f.amount
        elif f.type == models.TransactionType.income:
            income_by_category[f.category] += f.amount

    expenses_labels = list(expenses_by_category.keys())
    expenses_values = list(expenses_by_category.values())

    income_labels = list(income_by_category.keys())
    income_values = list(income_by_category.values())

    return templates.TemplateResponse(
        "finances/summary.html",
        {
            "request": request,
            "finances": finances,
            "total_income": summary["total_income"],
            "total_expenses": summary["total_expenses"],
            "balance": summary["balance"],
            "expenses_labels": expenses_labels,
            "expenses_values": expenses_values,
            "income_labels": income_labels,
            "income_values": income_values,
        },
    )


@router.post("/", response_class=RedirectResponse)
def create_finance(
    tipo: str = Form(...),
    monto: float = Form(...),
    categoria: str = Form(...),
    fecha: date = Form(...),
    db: Session = Depends(get_db)
):
    finance_data = schemas.FinanceCreate(
        type=schemas.TransactionType(tipo),
        amount=monto,
        category=categoria,
        date=fecha
    )
    finance_service.create_finance(db, finance_data)
    return RedirectResponse(url="/finances", status_code=HTTP_303_SEE_OTHER)


@router.get("/{finance_id}/edit", response_class=HTMLResponse)
def edit_finance_form(finance_id: int, request: Request, db: Session = Depends(get_db)):
    finance = finance_service.get_finance(db, finance_id)
    if not finance:
        return RedirectResponse(url="/finances", status_code=HTTP_303_SEE_OTHER)
    return templates.TemplateResponse(
        "finances/edit_finance.html",
        {"request": request, "finance": finance}
    )


@router.post("/{finance_id}/edit", response_class=RedirectResponse)
def update_finance(
    finance_id: int,
    tipo: str = Form(..., alias="tipo"),
    categoria: str = Form(..., alias="categoria"),
    amount: float = Form(..., alias="monto"),
    transaction_date: date = Form(..., alias="fecha"),
    db: Session = Depends(get_db)
):
    finance_data = schemas.FinanceUpdate(
        tipo=schemas.TransactionType(tipo),
        categoria=categoria,
        monto=amount,
        fecha=transaction_date
    )
    finance_service.update_finance(db, finance_id, finance_data)
    return RedirectResponse(url="/finances", status_code=HTTP_303_SEE_OTHER)


@router.post("/{finance_id}/delete", response_class=RedirectResponse)
def delete_finance(finance_id: int, db: Session = Depends(get_db)):
    finance_service.delete_finance(db, finance_id)
    return RedirectResponse(url="/finances", status_code=HTTP_303_SEE_OTHER)
