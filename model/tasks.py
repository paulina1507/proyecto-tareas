from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from config.db import engine, meta_data

tasks = Table(
    "tasks",
    meta_data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(255), nullable=False),
    Column("description", String(1000), nullable=True),
    Column("completed", Boolean, nullable=False, server_default="0"),
    Column("created_at", DateTime(timezone=True), server_default=func.now(), nullable=False),
    Column("updated_at", DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
)

