from fastapi import FastAPI 
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/check")
async def check():
    return{"message":"its running"}