# app/main.py
from tempfile import template
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.config import STATIC_DIR
from app.routes.router import router
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.models import finance, task, user, project

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(router) 

@app.get("/", response_class=HTMLResponse) 
async def root(request: Request):
    return template.TemplateResponse("home.html", {"request": request})