# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse # Make sure HTMLResponse is imported
from app.routes.router import router
from app.config import STATIC_DIR, templates # Ensure templates and STATIC_DIR are imported
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.models import finance, task, user

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(router) # Make sure your main router is included here

@app.get("/", response_class=HTMLResponse) # This is the crucial part for the root URL
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})