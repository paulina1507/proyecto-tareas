# 📌 API de Gestión de Tareas — FastAPI + MySQL

## 🛠 Instrucciones para ejecutar el proyecto

1. **Clonar el repositorio**
```bash
git clone https://github.com/tuusuario/proyecto-tareas.git
cd proyecto-tareas

2. **Crear y activar entorno virtual**

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. **Instalar dependencias**

pip install -r requirements.txt

4. **Configurar base de datos MySQL**

Crear una base de datos:


CREATE DATABASE tareasbd CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
Editar config/db.py con las credenciales correctas:

engine = create_engine("mysql+pymysql://usuario:contraseña@localhost:3306/tareasbd")

5. **Ejecutar el servidor**

uvicorn main:app --reload

API disponible en: http://127.0.0.1:8000
Documentación: http://127.0.0.1:8000/docs

📦 Dependencias necesarias
fastapi
uvicorn
sqlalchemy
pymysql
pydantic

Se instalan con:

pip install fastapi uvicorn sqlalchemy pymysql pydantic

📖 Breve explicación
Este sistema es una API REST que permite gestionar tareas personales.

Funciones principales:

Crear tareas con título y descripción.
Listar tareas almacenadas en MySQL.
Actualizar el estado o información de una tarea como su estado completado/no completado.
Eliminar tareas existentes.

La API usa FastAPI para manejar las rutas y peticiones, SQLAlchemy para interactuar con MySQL y Pydantic para validar los datos..
