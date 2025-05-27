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
│   │   ├── user.py
│   │   ├── finance.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── finance.py
│   │   └── task.py
│   ├── routes/
│   │   ├── finance_router.py
│   │   ├── task_routes.py
│   │   └── router.py
│   ├── services/
│   │   ├── finance_service.py
│   │   └── task_service.py
│   ├── templates/
|   |   ├── base.html
|   │   └── home.html
│   │   ├── finances/
|   |   |   ├── base_finance.html
|   |   |   ├── edit_finance.html
|   |   |   ├── summary.html
|   │   │   └── transactions.html 
│   │   └── projects/
|   |   |   ├── create_task.html
|   |   |   ├── edit_task.html
|   |   |   ├── list_projects.html
|   │   │   └── task_projects.html 
│   │   └── static/
│   │   |   ├── js/
|   │   │   └── charts.js
├── .gitignore
├── requirements.txt
├── README.md
````