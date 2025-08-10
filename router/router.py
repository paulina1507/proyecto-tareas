from fastapi import APIRouter, HTTPException
from sqlalchemy import select, insert, update, delete, func
from sqlalchemy.engine import Result
from config.db import engine
from model.tasks import tasks
from schema.task_schema import TaskCreate, TaskUpdate, TaskOut

router = APIRouter()

def row_to_dict(row) -> dict:
    # Convierte Row -> dict manejando None/boolean de MySQL
    d = dict(row._mapping)
    d["completed"] = bool(d.get("completed", 0))
    return d

@router.get("/", tags=["root"])
def root():
    return {"message": "Gestor de Tareas"}

# GET /tasks
@router.get("/tasks", response_model=list[TaskOut], tags=["tasks"])
def get_tasks():
    with engine.connect() as conn:
        result: Result = conn.execute(select(tasks).order_by(tasks.c.id.desc()))
        return [row_to_dict(r) for r in result.fetchall()]

# POST /tasks
@router.post("/tasks", response_model=TaskOut, status_code=201, tags=["tasks"])
def create_task(payload: TaskCreate):
    with engine.begin() as conn:  # begin => commit automático
        res = conn.execute(
            insert(tasks).values(
                title=payload.title,
                description=payload.description,
                # completed se va por default = 0 en la BD
            )
        )
        new_id = res.inserted_primary_key[0]
        row = conn.execute(select(tasks).where(tasks.c.id == new_id)).fetchone()
        return row_to_dict(row)

# PUT /tasks/{id}
@router.put("/tasks/{task_id}", response_model=TaskOut, tags=["tasks"])
def update_task(task_id: int, payload: TaskUpdate):
    with engine.begin() as conn:
        # Verifica existencia
        row = conn.execute(select(tasks).where(tasks.c.id == task_id)).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Task not found")

        values = {}
        if payload.title is not None:
            values["title"] = payload.title
        if payload.description is not None:
            values["description"] = payload.description
        if payload.completed is not None:
            values["completed"] = payload.completed
        values["updated_at"] = func.now()

        if values:
            conn.execute(update(tasks).where(tasks.c.id == task_id).values(**values))

        row2 = conn.execute(select(tasks).where(tasks.c.id == task_id)).fetchone()
        return row_to_dict(row2)

# DELETE /tasks/{id}
@router.delete("/tasks/{task_id}", status_code=204, tags=["tasks"])
def delete_task(task_id: int):
    with engine.begin() as conn:
        res = conn.execute(delete(tasks).where(tasks.c.id == task_id))
        if res.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found")
    return None
