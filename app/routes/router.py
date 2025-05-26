# app/routes/router.py
from datetime import date
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.task import TaskCreate
from app.services.task_service import create_task, get_tasks
from app.config import templates

# IMPORTA TUS SUB-ROUTERS ESPECÍFICOS AQUÍ
from .finance_routes import router as finance_router_instance # Cambiado el nombre para evitar conflictos
from .task_routes import router as task_router_instance # Cambiado el nombre para evitar conflictos

router = APIRouter()

# INCLUYE LOS SUB-ROUTERS EN EL ROUTER PRINCIPAL
router.include_router(finance_router_instance, prefix="/finances", tags=["finances"]) # Añade un prefijo para /finances
router.include_router(task_router_instance, prefix="/tasks", tags=["tasks"]) # Añade un prefijo para /tasks


@router.get("/tasks", response_class=HTMLResponse)
def tasks_page(request: Request, db: Session = Depends(get_db)):
    tasks = get_tasks(db)
    return templates.TemplateResponse("projects/task_projects.html", {"request": request, "tasks": tasks})

@router.post("/tasks")
def add_task(
    title: str = Form(...),
    description: str = Form(...),
    priority: str = Form(...),
    deadline: date = Form(...),
    db: Session = Depends(get_db)
):
    task_data = TaskCreate(
        title=title,
        description=description,
        priority=priority,
        deadline=deadline
    )
    create_task(db, task_data)
    return RedirectResponse(url="/tasks", status_code=303)