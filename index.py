from fastapi import FastAPI
from models.note import note

app = FastAPI()
app.include_router(note)