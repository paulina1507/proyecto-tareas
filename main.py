from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.router import router as tasks_router

app = FastAPI(title="Todo API (MySQL)", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ajusta si ya tienes frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks_router)

@app.get("/health")
def health():
    return {"ok": True}
