from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session 
from app.db.session import engine
from app.db.base import Base
from app.db.__init__db import init_db
from app.api.deps import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/check")
async def check():
    return {"message": "its running"}

@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    return {"status": "db works"}

@app.on_event("startup")
def on_startup():
    init_db()