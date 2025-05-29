# Proyecto Finanzas y Tareas (Personal Manager)

Autor: **Maicol Stiven Aristizabal Salazar**
Fecha:**27/05/2025**
Curso:**Programación 2**
## 🧠 Descripción General

## Introducción
Este proyecto nace como una solución integral a los desafíos que enfrentan muchas personas al intentar gestionar sus tareas y finanzas de forma separada y desorganizada. Combina en una sola plataforma web, accesible desde cualquier dispositivo, la capacidad de administrar proyectos, tareas y su progreso, junto con el control de ingresos, gastos y saldos financieros. Utiliza programación orientada a objetos mediante clases como `Tarea`, `Proyecto`, `Gasto`, `Ingreso` y `Usuario`, aplicando principios de herencia, encapsulamiento y polimorfismo. Además, la aplicación incorpora gráficos simples para visualizar estadísticas y sigue buenas prácticas de desarrollo como modularidad, cohesión y documentación clara.

Aplicación web desarrollada con **FastAPI**, **SQLAlchemy** y **Jinja2**, que permite gestionar finanzas y tareas de manera eficiente, incluyendo control de estados, fechas de vencimiento y eliminación automática de tareas completadas, en la sección de proyectos, en la parte de finanzas incluye poder ingresar gastos e ingresos de cualquier categoría, te muestra tu balance y estadísticas.  

## Objetivos
- Diseñar e implementar una aplicación web multiplataforma accesible desde
computadoras y dispositivos móviles.
- Permitir el registro, edición, eliminación y visualización de tareas organizadas por proyecto, prioridad y estado.
- Registrar ingresos y gastos del usuario con categorías personalizables y visualización de saldos.
- Aplicar programación orientada a objetos mediante clases como Tarea, Proyecto, Gasto, Ingreso y Usuario, usando herencia, encapsulamiento y
polimorfismo.
- Visualizar estadísticas financieras y de tareas mediante gráficos simples para facilitar el análisis personal.
- Seguir buenas prácticas de desarrollo como modularidad, cohesión, bajo acoplamiento y documentación clara del código.

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

## Estructura del Proyecto

El proyecto está organizado en varios módulos dentro del directorio `app/`:

- `models/`: Define las clases que representan las entidades del sistema (usando SQLAlchemy).
- `schemas/`: Define los esquemas de validación y serialización de datos (usando Pydantic).
- `routes/`: Contiene las rutas de la API que gestionan la lógica de negocio.
- `database.py`: Configura la conexión y sesión con la base de datos.
- `main.py`: Punto de entrada de la aplicación.

---

## Diseño Orientado a Objetos de Proyecto_Finanzas_Tareas

**Proyecto:** Proyecto_Finanzas_Tareas
**Repositorio:** [Maicol1044/Proyecto_Finanzas_Tareas](https://github.com/Maicol1044/Proyecto_Finanzas_Tareas)

**Estructura del Proyecto**
El proyecto organiza su código en módulos dentro del directorio `app/`:

* `models/`: Define las clases que representan las entidades del sistema, utilizando SQLAlchemy para la interacción con la base de datos.

**Estructura del Proyecto**
El proyecto organiza su código en módulos dentro del directorio `app/`:

* `models/`: Define las clases que representan las entidades del sistema (utilizando SQLAlchemy).

**Clases y Atributos**

1.  **Clase: Finance**
    * Ubicación: `models/finance.py`
    * **Atributos:**
        * `id`: Identificador único de la transacción financiera.
        * `amount`: Monto de la transacción.
        * `description`: Descripción detallada de la transacción.
        * `date`: Fecha en la que se realizó la transacción.

2.  **Clase: Task**
    * Ubicación: `models/task.py`
    * **Atributos:**
        * `id`: Identificador único de la tarea.
        * `title`: Título o nombre de la tarea.
        * `description`: Descripción detallada de la tarea.
        * `due_date`: Fecha límite para completar la tarea.
        * `completed`: Estado booleano que indica si la tarea ha sido completada (`True`) o no (`False`).

**Relaciones Entre Clases**

Actualmente, basándonos en que la funcionalidad de usuario para iniciar sesión no está en uso, no se observan relaciones directas entre las clases `Finance` y `Task` en el código que has compartido. Ambas entidades existen de forma independiente en este contexto.

**Métodos (Implementados en los Controladores - `routes/`)**

La lógica de negocio y las operaciones (métodos) se encuentran en los controladores (`routes/`). Estos gestionan las interacciones con las entidades `Finance` y `Task`:

* **Operaciones de Finanzas:**
    * Creación de nuevas transacciones financieras.
    * Listado de transacciones financieras.
    * Actualización de la información de una transacción financiera existente.
    * Eliminación de una transacción financiera.
* **Operaciones de Tareas:**
    * Creación de nuevas tareas.
    * Obtención de todas las tareas.
    * Marcado de una tarea como completada.
    * Implementación de la eliminación automática de tareas que han sido marcadas como completadas.

**Justificación de las Decisiones de Diseño**

A pesar de no tener una relación explícita con un usuario autenticado en la funcionalidad actual, el diseño orientado a objetos sigue ofreciendo beneficios:

* **Separación de Responsabilidades:** Los modelos (`Finance`, `Task`) se centran en la estructura de los datos, mientras que los controladores manejan la lógica de negocio. Esto facilita la organización del código.
* **Modelado del Dominio:** Las clases representan las entidades clave de la aplicación de finanzas y tareas.
* **Reusabilidad:** Los modelos pueden ser reutilizados si en el futuro decides implementar la funcionalidad de usuario.
* **Facilita la Extensibilidad:** Si decides agregar nuevas entidades relacionadas con finanzas o tareas, la estructura POO facilita su incorporación.

En este escenario específico, aunque la clase `User` y sus relaciones no estén activas, el diseño POO sienta una base sólida para futuras expansiones de la aplicación.

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

## Pruebas realizadas
Las pruebas realizadas fueron por mí mismo, ensayando cada funcionalidad de la aplicación web para que todo funcionara correctamente

##Conclusiones
# Logros
Pude dominar FastAPI, dominar bases de datos, pude dominar Git y mejoré mucho en la organización de código y arquitectura

# Desafíos
Esto me llevó desafíos técnicos como el diseño de la base de datos, el manejo de errores y la validación de datos. También se presentan desafíos en el diseño de la interfaz y la experiencia del usuario,

# Lecciones aprendidas
Este proyecto me enseñó la importancia d eplanificar y diseñar bien una aplicación resaltando el valor de la modularidad y la separación de responsabilidades

# Posibles mejoras futuras
La aplicación tiene muchos aspectos a mejorar pero el principal sería integrar lo del usuario, que todo el que entre pueda de alguna o otra manera iniciar sesión

## Diagrama de Clases UML
Puse esto al final porque me quitaba el formato de todo lo que estuvier abajo

```plantuml
@startuml
class Finance {
  -id: int
  -amount: float
  -description: str
  -date: date
}

class Task {
  -id: int
  -title: str
  -description: str
  -due_date: date
  -completed: bool
}

@enduml
