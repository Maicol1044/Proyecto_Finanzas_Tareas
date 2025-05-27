# Proyecto Finanzas y Tareas (Personal Manager)

Autor: **Maicol Stiven Aristizabal Salazar**
Fecha:**27/05/2025**

## 🧠 Descripción General

Este proyecto nace como una solución integral a los desafíos que enfrentan muchas personas al intentar gestionar sus tareas y finanzas de forma separada y desorganizada. Combina en una sola plataforma web, accesible desde cualquier dispositivo, la capacidad de administrar proyectos, tareas y su progreso, junto con el control de ingresos, gastos y saldos financieros. Utiliza programación orientada a objetos mediante clases como `Tarea`, `Proyecto`, `Gasto`, `Ingreso` y `Usuario`, aplicando principios de herencia, encapsulamiento y polimorfismo. Además, la aplicación incorpora gráficos simples para visualizar estadísticas y sigue buenas prácticas de desarrollo como modularidad, cohesión y documentación clara.

Aplicación web desarrollada con **FastAPI**, **SQLAlchemy** y **Jinja2**, que permite gestionar finanzas y tareas de manera eficiente, incluyendo control de estados, fechas de vencimiento y eliminación automática de tareas completadas, en la sección de proyectos, en la parte de finanzas incluye poder ingresar gastos e ingresos de cualquier categoría, te muestra tu balance y estadísticas.  


---

## Funcionalidades proyectos
- Crear, editar y eliminar proyectos
- Asociar tareas a proyectos
- Seguimiento del estado de las tareas: `pending`, `in_progress`, `completed`
- Establecer fechas de vencimiento
- Eliminación automática de tareas marcadas como completadas (en segundo plano)
- Interfaz HTML basada en Jinja2 y Bootstrap

## Funcionalidades finanzas
-Crear, editar y categorizar ingresos y egresos
-Asocia tus gastos con tus ganancias y te da el balance
-Se puede modificar cualquier cosa en caso de cometer algún error
- Interfaz HTML basada en Jinja2 y Bootstrap
---

## Estructura del Proyecto

```
MI_PROYECTO_PROGRAMACION_II/
├──app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── models/
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── finance.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── finance.py
│   │   └── task.py
│   ├── routes/
│   │   ├── finance_routes.py
│   │   ├── project_routes.py
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
|   |   |   ├── create_project.html
|   |   |   ├── edit_task.html
|   |   |   ├── edit_project.html
|   |   |   ├── list_projects.html
|   │   │   └── task_projects.html 
│   │   └── static/
│   │   |   ├── js/
|   │   │   └── charts.js
├── .gitignore
├── requirements.txt
├── README.md
```

# Proyecto: Proyecto_Finanzas_Tareas - Diseño POO

Repositorio: [Maicol1044/Proyecto_Finanzas_Tareas](https://github.com/Maicol1044/Proyecto_Finanzas_Tareas)

## Estructura del Proyecto

El proyecto está organizado en varios módulos dentro del directorio `app/`:

- `models/`: Define las clases que representan las entidades del sistema (usando SQLAlchemy).
- `schemas/`: Define los esquemas de validación y serialización de datos (usando Pydantic).
- `routes/`: Contiene las rutas de la API que gestionan la lógica de negocio.
- `database.py`: Configura la conexión y sesión con la base de datos.
- `main.py`: Punto de entrada de la aplicación.

---

## Clases y Relaciones

### 1. `User`

- **Ubicación**: `models/user.py`
- **Atributos**:
  - `id`: Identificador único del usuario.
  - `username`: Nombre de usuario.
  - `email`: Correo electrónico.
  - `password`: Contraseña cifrada.
- **Relaciones**:
  - Un usuario puede tener múltiples objetos `Finance` y `Task`.

---

### 2. `Finance`

- **Ubicación**: `models/finance.py`
- **Atributos**:
  - `id`: Identificador único de la transacción.
  - `amount`: Monto de la transacción.
  - `description`: Descripción.
  - `date`: Fecha de la transacción.
  - `user_id`: Referencia al usuario propietario.
- **Relaciones**:
  - Relación muchos-a-uno con `User`.

---

### 3. `Task`

- **Ubicación**: `models/task.py`
- **Atributos**:
  - `id`: Identificador único de la tarea.
  - `title`: Título de la tarea.
  - `description`: Descripción.
  - `due_date`: Fecha de vencimiento.
  - `completed`: Estado (booleano).
  - `user_id`: Referencia al usuario propietario.
- **Relaciones**:
  - Relación muchos-a-uno con `User`.

---

## Relaciones Entre Clases

Las relaciones están modeladas con SQLAlchemy:

- **User 1:N Finance**
- **User 1:N Task**

Cada instancia de `Finance` o `Task` pertenece a un único `User` a través de la clave foránea `user_id`.

---

## Métodos

Los métodos están definidos principalmente en los controladores (`routes/`) y gestionan operaciones CRUD:

### Usuarios
- Registro de nuevos usuarios.
- Autenticación y manejo de sesiones.

### Finanzas
- Crear transacciones financieras.
- Listar transacciones por usuario.
- Actualizar y eliminar transacciones.

### Tareas
- Crear tareas nuevas.
- Obtener tareas por usuario.
- Marcar tareas como completadas.
- Eliminar tareas automáticamente si están completadas.

---

## Conclusión

Este diseño orientado a objetos proporciona:

- Separación clara de responsabilidades (modelo, esquema, ruta).
- Escalabilidad para añadir nuevas entidades.
- Mantenibilidad en la lógica de negocio.

Puedes extender el proyecto fácilmente siguiendo esta estructura modular y reutilizable.

---

## Instalación

```bash
# 1. Clona este repositorio
git clone https://github.com/Maicol1044/Proyecto_Finanzas_Tareas.git
cd Proyecto_Finanzas_Tareas

# 2. Crea un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instala las dependencias
pip install -r requirements.txt

## Ejecución del proyecto
uvicorn main:app --reload
Accede desde tu navegador a: http://localhost:8000