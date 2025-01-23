from fastapi import APIRouter,Depends, Path,status,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import Field, BaseModel
import sys 
sys.path.insert(0, "./../" )
from database import get_db
from models import AtpPlayers,AtpSingles
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
async def get_first_10_players(db:db_dependency):
    return db.query(AtpPlayers).limit(10).all()

@router.get("/matches/head-to-head", status_code=status.HTTP_200_OK)
async def get_head_to_head(
    player1_id: int,
    player2_id: int,
    db: db_dependency
):
    """Get head-to-head statistics between two players"""
    # Matches where player1 won against player2
    p1_wins = db.query(AtpSingles).filter(
        AtpSingles.winner_id == player1_id,
        AtpSingles.loser_id == player2_id
    ).count()
    
    # Matches where player2 won against player1
    p2_wins = db.query(AtpSingles).filter(
        AtpSingles.winner_id == player2_id,
        AtpSingles.loser_id == player1_id
    ).count()
    
    return {
        "player1_wins": p1_wins,
        "player2_wins": p2_wins,
        "total_matches": p1_wins + p2_wins
    }


    
    
