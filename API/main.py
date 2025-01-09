from fastapi import FastAPI,Depends,status,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db
from models import Singles

app= FastAPI()

db_dependency=Annotated[Session,Depends(get_db)]


@app.get("/singles_matches_100",status_code=status.HTTP_200_OK)
async def get_first_100_singles_matches(db:db_dependency):
    return db.query(Singles).limit(10).all()

