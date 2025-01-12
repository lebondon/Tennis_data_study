from fastapi import FastAPI,Depends,status,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db
from models import *
from routers import players

app= FastAPI()

db_dependency=Annotated[Session,Depends(get_db)]

app.include_router(players.router)

@app.get("/",status_code=status.HTTP_200_OK)
async def get_first_100_singles_matches(db:db_dependency):
    return db.query(AtpSingles).limit(10).all()



