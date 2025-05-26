# app/routes/task_routes.py
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
# from fastapi.templating import Jinja2Templates # REMOVE THIS LINE
from sqlalchemy.orm import Session
from datetime import datetime

from ..schemas.task import TaskCreate
from ..services.task_service import create_task, get_tasks
from ..database import get_db
from app.config import templates # <-- ADD THIS IMPORT

router = APIRouter()
# templates = Jinja2Templates(directory="app/templates") # <-- DELETE THIS LINE

@router.get("/tareas", response_class=HTMLResponse)
def tasks_page(request: Request, db: Session = Depends(get_db)):
    tasks = get_tasks(db)
    return templates.TemplateResponse("proyectos/tareas_proyectos.html", {"request": request, "tasks": tasks})

@router.post("/tareas")
def add_task(
    title: str = Form(..., alias="titulo"),
    description: str = Form(..., alias="descripcion"),
    priority: str = Form(..., alias="prioridad"),
    deadline: str = Form(..., alias="fecha_vencimiento"),
    db: Session = Depends(get_db)
):
    deadline_dt = datetime.strptime(deadline, "%Y-%m-%d")
    task_data = TaskCreate(
        title=title,
        description=description,
        priority=priority,
        deadline=deadline_dt
    )
    create_task(db, task_data)
    return RedirectResponse(url="/tareas", status_code=303)
