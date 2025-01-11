from fastapi import FastAPI,Depends,status,HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db
from models import *

app= FastAPI()

db_dependency=Annotated[Session,Depends(get_db)]


@app.get("/",status_code=status.HTTP_200_OK)
async def get_first_100_singles_matches(db:db_dependency):
    return db.query(AtpSingles).limit(10).all()

@app.get("/analytics/head2head/", status_code=status.HTTP_200_OK)
async def get_head_to_head(
    db: db_dependency,
    player1_id: int,
    player2_id: int
):
    """Get head-to-head statistics between two players"""
    # Matches where player1 won against player2
    p1_wins = db.query(AtpSingles).\
        filter(AtpSingles.winner_id == player1_id, AtpSingles.loser_id == player2_id).count()
    
    # Matches where player2 won against player1
    p2_wins = db.query(AtpSingles).\
        filter(AtpSingles.winner_id == player2_id, AtpSingles.loser_id == player1_id).count()
    
    return {
        "player1_wins": p1_wins,
        "player2_wins": p2_wins,
        "total_matches": p1_wins + p2_wins
    }

