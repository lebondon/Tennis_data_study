from fastapi import FastAPI,Depends,status,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db

app= FastAPI()

db_dependency=Annotated[Session,Depends(get_db)]


@app.get("/",status_code=status.HTTP_200_OK)
async def get_all_matches(db:db_dependency):
    return db.query().all()