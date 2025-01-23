from fastapi import FastAPI, Depends, status, HTTPException, Request, Form, Query as FastAPIQuery
from typing import Annotated, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_, cast, BigInteger, literal, desc
from database import get_db
from models import *
from routers import players
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,JSONResponse


app = FastAPI(title="Tennis stats")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

db_dependency = Annotated[Session, Depends(get_db)]

app.include_router(players.router, prefix="/players", tags=["players"])

@app.get("/", status_code=status.HTTP_200_OK)
async def home(request: Request, db: db_dependency):
    """Homepage for the tennis stats application"""
    try:
        # Get total players (combining ATP and WTA players)
        total_players = db.query(AtpPlayers).count() + db.query(WtaPlayers).count()
        
        # Get total matches (combining all match types)
        total_matches = (
            db.query(AtpSingles).count() +
            db.query(AtpDoubles).count() +
            db.query(WtaSingles).count() +
            db.query(AtpFutures).count() +
            db.query(AtpQuallChall).count()
        )
        
        # Get total tournaments
        total_tournaments = db.query(TotalTourneys).count()
        
    except Exception as e:
        print(f"Error fetching stats: {e}")
        total_players = 0
        total_matches = 0
        total_tournaments = 0
    
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "total_players": "{:,}".format(total_players),
            "total_matches": "{:,}".format(total_matches),
            "total_tournaments": "{:,}".format(total_tournaments)
        }
    )
    
# Add this route to main.py
@app.get("/search-players", response_class=JSONResponse)
async def search_players(
    request: Request,
    query: str,
    db: db_dependency
):
    """AJAX endpoint for player search"""
    if len(query) < 2:
        return []
        
    search_query = f"%{query}%"
    
    # Search in both ATP and WTA players
    atp_players = (
        db.query(AtpPlayers)
        .filter(
            or_(
                AtpPlayers.name_full.ilike(search_query),
                AtpPlayers.name_first.ilike(search_query),
                AtpPlayers.name_last.ilike(search_query)
            )
        )
        .limit(5)
        .all()
    )
    
    wta_players = (
        db.query(WtaPlayers)
        .filter(
            or_(
                WtaPlayers.name_full.ilike(search_query),
                WtaPlayers.name_first.ilike(search_query),
                WtaPlayers.name_last.ilike(search_query)
            )
        )
        .limit(5)
        .all()
    )
    
    # Format results with tour indication
    results = []
    
    # Add ATP players
    results.extend([{
        "id": str(p.player_id),  # Convert to string to ensure JSON compatibility
        "name": p.name_full,
        "country": p.ioc if p.ioc else "",
        "tour": "ATP"
    } for p in atp_players])
    
    # Add WTA players
    results.extend([{
        "id": str(p.player_id),  # Convert to string to ensure JSON compatibility
        "name": p.name_full,
        "country": p.ioc if p.ioc else "",
        "tour": "WTA"
    } for p in wta_players])
    
    return results





    
@app.get("/head-to-head", response_class=HTMLResponse)
async def head_to_head_page(request: Request):
    """Render the head to head search page"""
    return templates.TemplateResponse(
        "head_to_head.html",
        {"request": request}
    )
    
    
    
    

def get_atp_matches_query(db, player1_id, player2_id):
    """Get matches from all ATP tables"""
    from sqlalchemy import text, cast, BigInteger, desc

    # Convert player IDs to integer
    player1_id = int(player1_id)
    player2_id = int(player2_id)

    # ATP Singles matches
    query = (
        db.query(
            AtpSingles.match_id,
            AtpSingles.match_num,
            AtpSingles.winner_id,
            AtpSingles.loser_id,
            AtpSingles.score,
            AtpSingles.round,
            AtpSingles.minutes,
            AtpPlayers.name_full.label('winner_name'),
            TotalTourneys.tourney_name.label('tournament_name')
        )
        .join(
            AtpPlayers,
            cast(AtpSingles.winner_id, BigInteger) == cast(AtpPlayers.player_id, BigInteger)
        )
        .join(
            TotalTourneys,
            AtpSingles.tourney_id == TotalTourneys.tourney_name_date_matches
        )
        .filter(
            or_(
                (cast(AtpSingles.winner_id, BigInteger) == player1_id) & 
                (cast(AtpSingles.loser_id, BigInteger) == player2_id),
                (cast(AtpSingles.winner_id, BigInteger) == player2_id) & 
                (cast(AtpSingles.loser_id, BigInteger) == player1_id)
            )
        )
        .order_by(desc(AtpSingles.match_num))
    )
    
    return query






def get_wta_matches_query(db, player1_id, player2_id):
    """Get matches from all WTA tables"""
    from sqlalchemy import text, cast, BigInteger, desc

    # Convert player IDs to integer
    player1_id = int(player1_id)
    player2_id = int(player2_id)

    # WTA Singles matches
    query = (
        db.query(
            WtaSingles.match_id,
            WtaSingles.match_num,
            WtaSingles.winner_id,
            WtaSingles.loser_id,
            WtaSingles.score,
            WtaSingles.round,
            WtaSingles.minutes,
            WtaPlayers.name_full.label('winner_name'),
            TotalTourneys.tourney_name.label('tournament_name')
        )
        .join(
            WtaPlayers,
            cast(WtaSingles.winner_id, BigInteger) == cast(WtaPlayers.player_id, BigInteger)
        )
        .join(
            TotalTourneys,
            WtaSingles.tourney_id == TotalTourneys.tourney_name_date_matches
        )
        .filter(
            or_(
                (cast(WtaSingles.winner_id, BigInteger) == player1_id) & 
                (cast(WtaSingles.loser_id, BigInteger) == player2_id),
                (cast(WtaSingles.winner_id, BigInteger) == player2_id) & 
                (cast(WtaSingles.loser_id, BigInteger) == player1_id)
            )
        )
        .order_by(desc(WtaSingles.match_num))
    )
    
    return query





@app.post("/head-to-head-results")
@app.get("/head-to-head-results")
async def get_head_to_head_results(
    request: Request,
    db: db_dependency,
    player1_id: Optional[int] = None,
    player2_id: Optional[int] = None,
    page: int = FastAPIQuery(1, ge=1),
    per_page: int = FastAPIQuery(10, ge=1, le=50)
):
    """Get and render head-to-head results"""
    try:
        # Handle both POST and GET methods
        if request.method == "POST":
            form = await request.form()
            player1_id_str = form.get("player1_id")
            player2_id_str = form.get("player2_id")
            
            # Validate form inputs
            if not player1_id_str or not player2_id_str:
                return templates.TemplateResponse(
                    "head_to_head.html",
                    {
                        "request": request,
                        "error": "Please select both players"
                    }
                )
            
            try:
                player1_id = int(player1_id_str)
                player2_id = int(player2_id_str)
            except ValueError:
                return templates.TemplateResponse(
                    "head_to_head.html",
                    {
                        "request": request,
                        "error": "Invalid player selection"
                    }
                )
        
        if not player1_id or not player2_id:
            return templates.TemplateResponse(
                "head_to_head.html",
                {"request": request}
            )

        # Get tour type from player search
        player1_tour = form.get("player1_tour")
        player2_tour = form.get("player2_tour")

        print(f"Player 1 ID: {player1_id}, Tour: {player1_tour}")
        print(f"Player 2 ID: {player2_id}, Tour: {player2_tour}")

        # Check if players are from the same tour
        if player1_tour != player2_tour:
            return templates.TemplateResponse(
                "head_to_head.html",
                {
                    "request": request,
                    "error": f"Players must be from the same tour. Player 1 is from {player1_tour}, Player 2 is from {player2_tour}."
                }
            )

        # Look up players based on tour
        if player1_tour == "ATP":
            player1 = db.query(AtpPlayers).filter(AtpPlayers.player_id == player1_id).first()
            player2 = db.query(AtpPlayers).filter(AtpPlayers.player_id == player2_id).first()
            matches_query = get_atp_matches_query(db, player1_id, player2_id)
            tour = "ATP"
        else:  # WTA
            player1 = db.query(WtaPlayers).filter(WtaPlayers.player_id == player1_id).first()
            player2 = db.query(WtaPlayers).filter(WtaPlayers.player_id == player2_id).first()
            matches_query = get_wta_matches_query(db, player1_id, player2_id)
            tour = "WTA"

        if not player1 or not player2:
            return templates.TemplateResponse(
                "head_to_head.html",
                {
                    "request": request,
                    "error": "One or both players not found in the database"
                }
            )

        # Get matches and process results
        matches = matches_query.all()
        total_matches = len(matches)

        # Count wins for each player
        p1_wins = sum(1 for match in matches if str(match.winner_id) == str(player1_id))
        p2_wins = sum(1 for match in matches if str(match.winner_id) == str(player2_id))

        # Calculate pagination
        total_pages = max(1, (total_matches + per_page - 1) // per_page)
        page = min(page, total_pages)
        
        # Calculate showing_matches info
        showing_matches = {
            "start": (page - 1) * per_page + 1 if total_matches > 0 else 0,
            "end": min(page * per_page, total_matches)
        }
        
        # Get paginated results
        start_idx = (page - 1) * per_page
        end_idx = start_idx + per_page
        paginated_matches = matches[start_idx:end_idx]
        
        return templates.TemplateResponse(
            "head_to_head.html",
            {
                "request": request,
                "player1": player1,
                "player2": player2,
                "tour": tour,
                "matches": paginated_matches,
                "total_matches": total_matches,
                "p1_wins": p1_wins,
                "p2_wins": p2_wins,
                "current_page": page,
                "total_pages": total_pages,
                "per_page": per_page,
                "has_next": page < total_pages,
                "has_prev": page > 1,
                "showing_matches": showing_matches
            }
        )
    except Exception as e:
        import traceback
        print(f"Error in head-to-head results: {str(e)}")
        print(traceback.format_exc())
        return templates.TemplateResponse(
            "head_to_head.html",
            {
                "request": request,
                "error": f"An error occurred while retrieving match data: {str(e)}"
            }
        )
        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


