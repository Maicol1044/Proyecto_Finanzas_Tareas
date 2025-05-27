# app/routes/project_routes.py

from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from app.config import templates
from app.database import get_db
from app.models.project import Project

router = APIRouter()

@router.get("/projects", response_class=HTMLResponse)
def list_projects(request: Request, db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return templates.TemplateResponse("projects/list_projects.html", {
        "request": request,
        "projects": projects
    })

@router.get("/projects/create", response_class=HTMLResponse)
def create_project_form(request: Request):
    return templates.TemplateResponse("projects/create_project.html", {
        "request": request
    })

@router.post("/projects/create")
def create_project(
    name: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):
    new_project = Project(name=name, description=description)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return RedirectResponse(url="/projects", status_code=303)
