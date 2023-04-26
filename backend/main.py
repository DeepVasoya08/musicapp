from fastapi import FastAPI

from .db import SessionLocal
from .routes import auth, user


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
async def root():
    return "OK"


app.include_router(auth.router)
app.include_router(user.router)
