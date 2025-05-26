# app/config.py
import os
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates # Asegúrate de que esto esté
from fastapi.staticfiles import StaticFiles # Asegúrate de que esto esté importado

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# --- Asegúrate de que esta línea exista y sea correcta ---
STATIC_DIR = os.path.join(BASE_DIR, "static")
# --- Fin de la sección a verificar ---

