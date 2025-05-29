# app/routes/router.py
from datetime import date
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project  
from app.schemas.task import TaskCreate
from app.services.task_service import create_task, get_tasks
from app.config import templates
from app.models.task import Task
from .project_routes import router as project_router_instance

from .finance_routes import router as finance_router_instance 
from .task_routes import router as task_router_instance 

router = APIRouter()
router.include_router(project_router_instance, tags=["projects"])
router.include_router(finance_router_instance, prefix="/finances", tags=["finances"]) 
router.include_router(task_router_instance, tags=["tasks"])

@router.get("/projects/{project_id}/tasks", response_class=HTMLResponse)
def tasks_page(request: Request, project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).get(project_id)  
    if not project:
        return HTMLResponse(content="Proyecto no encontrado", status_code=404)
    
    tasks = db.query(Task).filter(Task.project_id == project_id).all()  
    
    return templates.TemplateResponse(
        "projects/task_projects.html",
        {
            "request": request,
            "tasks": tasks,
            "project": project,         
            "project_id": project.id    
        }
    )

@router.post("/projects/{project_id}/tasks")
def add_task(
    project_id: int,
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
        deadline=deadline,
        project_id=project_id  
    )
    create_task(db, task_data)
    return RedirectResponse(url=f"/projects/{project_id}/tasks", status_code=303)

@router.get("/tasks/{task_id}/edit", response_class=HTMLResponse)
def edit_task_form(task_id: int, request: Request, db: Session = Depends(get_db)):
    task = db.query(Task).get(task_id)
    if not task:
        return HTMLResponse("Tarea no encontrada", status_code=404)
    
    return templates.TemplateResponse("projects/edit_task.html", {
        "request": request,
        "task": task
    })
