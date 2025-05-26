**Cree y activé un entorno virtual**
python -m venv .venv
.\\env\Scripts\activate
**Instalé y guardé todas las dependencias que necesitaba**

pip install -r requirements.txt
pip freeze > requirements.txt
````
MI_PROYECTO_PROGRAMACION_II/
├──app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── finance.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── finance.py
│   │   └── task.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── router.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── finance_service.py
│   │   └── task_service.py
├── .gitignore
├── requirements.txt
├── README.md
````