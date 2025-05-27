# app/routes/task_routes.py
from fastapi import APIRouter, Request, Form, Depends, BackgroundTasks, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from app.config import templates
from app.database import SessionLocal
from app.models.project import Project  # type: ignore
from app.models.task import Task        # type: ignore
from sqlalchemy.orm import Session
from datetime import date

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función de eliminación en segundo plano
def delete_completed_task(task_id: int):
    db = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if task and task.status == "completed":
            db.delete(task)
            db.commit()
    finally:
        db.close()

# Rutas de proyectos
@router.get("/projects", response_class=HTMLResponse)
def list_projects(request: Request, db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return templates.TemplateResponse("list_projects.html", {"request": request, "projects": projects})

@router.get("/projects/create", response_class=HTMLResponse)
def create_project_form(request: Request):
    return templates.TemplateResponse("create_project.html", {"request": request})

@router.post("/projects/create")
def create_project(name: str = Form(...), description: str = Form(...), db: Session = Depends(get_db)):
    project = Project(name=name, description=description)
    db.add(project)
    db.commit()
    return RedirectResponse("/projects", status_code=303)

@router.get("/projects/{project_id}/edit", response_class=HTMLResponse)
def edit_project_form(project_id: int, request: Request, db: Session = Depends(get_db)):
    project = db.query(Project).get(project_id)
    return templates.TemplateResponse("edit_project.html", {"request": request, "project": project})

@router.post("/projects/{project_id}/edit")
def edit_project(project_id: int, name: str = Form(...), description: str = Form(...), db: Session = Depends(get_db)):
    project = db.query(Project).get(project_id)
    project.name = name
    project.description = description
    db.commit()
    return RedirectResponse("/projects", status_code=303)

@router.post("/projects/{project_id}/delete")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).get(project_id)
    db.delete(project)
    db.commit()
    return RedirectResponse("/projects", status_code=303)

# ✅ NUEVA RUTA: Marcar tarea como completada y eliminarla en segundo plano
@router.post("/tasks/{task_id}/complete")
def complete_task(task_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    task.status = "completed"
    db.commit()
    background_tasks.add_task(delete_completed_task, task_id)
    return RedirectResponse("/projects", status_code=303)

@router.get("/projects/{project_id}/tasks", response_class=HTMLResponse)
def view_tasks(request: Request, project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    tasks = db.query(Task).filter(Task.project_id == project_id).all()
    return templates.TemplateResponse("projects/task_projects.html", {
        "request": request,
        "project": project,
        "tasks": tasks,
        "project_id": project_id  # ✅ Esto es lo que se necesita en el HTML
    })
