from fastapi import APIRouter,Depends, Path,status,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import Field, BaseModel
import sys 
sys.path.insert(0, "./../" )
from database import get_db
from models import AtpPlayers
from database import SessionLocal 
from datetime import date

class PlayerRequest(BaseModel):
    player_id: int = Field(ge=10000,le=99999)
    name_first: str = Field(min_length=1)
    name_last: str = Field(min_length=1)
    hand: str = Field(max_length=1,min_length=1)
    dob: date 
    ioc: str = Field(max_length=3,min_length=3)
    height: int = Field(lt=250,gt=100)
    wikidata_id: str = Field(min_length=1)
    name_full: str = Field(min_length=3)
    
    
router=APIRouter()

db_dependency=Annotated[Session,Depends(get_db)]

@router.get("/",status_code=status.HTTP_200_OK)            
async def get_players(db:db_dependency):
    return db.query(AtpPlayers).limit(10).all()


    
    
