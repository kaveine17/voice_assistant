from fastapi import FastAPI
from database import engine, Base
import models 

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Backend + PostgreSQL работает 🚀"}