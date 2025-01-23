from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey,BigInteger,Boolean

class AtpSingles(Base):
    __tablename__='atp_singles_matches'

    match_id = Column(String, primary_key=True)
    match_num= Column(Integer)
    winner_id= Column(BigInteger,ForeignKey("atp_players.player_id"))
    winner_seed= Column(String)
    winner_entry=Column(String)
    winner_age=Column(BigInteger,default=False)
    loser_id=Column(BigInteger,ForeignKey("atp_players.player_id"))
    loser_seed=Column(String)
    loser_entry=Column(String)
    loser_age=Column(Float)
    score=Column(String)
    round=Column(String)
    minutes=Column(Integer)
    w_ace=Column(Integer)
    w_df=Column(Integer)
    w_svpt=Column(Integer)
    w_1stIn=Column(Integer)
    w_1stWon=Column(Integer)
    w_2ndWon=Column(Integer)
    w_SvGms=Column(Integer)
    w_bpSaved=Column(Integer)
    w_bpFaced=Column(Integer)
    l_ace=Column(Integer)
    l_df=Column(Integer)
    l_svpt=Column(Integer)
    l_1stIn=Column(Integer)
    l_1stWon=Column(Integer)
    l_2ndWon=Column(Integer)
    l_SvGms=Column(Integer)
    l_bpSaved=Column(Integer)
    l_bpFaced=Column(Integer)
    winner_rank=Column(Integer)
    winner_rank_points=Column(Integer)
    loser_rank=Column(Integer)
    loser_rank_points=Column(Integer)
    tourney_id=Column(String)
    
class AtpFutures(Base):
    __tablename__='atp_futures_matches'

    match_id = Column(String, primary_key=True)
    match_num= Column(Integer)
    winner_id= Column(BigInteger,ForeignKey("atp_players.player_id"))
    winner_seed= Column(String)
    winner_entry=Column(String)
    winner_age=Column(BigInteger,default=False)
    loser_id=Column(BigInteger,ForeignKey("atp_players.player_id"))
    loser_seed=Column(String)
    loser_entry=Column(String)
    loser_age=Column(Float)
    score=Column(String)
    round=Column(String)
    minutes=Column(Integer)
    w_ace=Column(Integer)
    w_df=Column(Integer)
    w_svpt=Column(Integer)
    w_1stIn=Column(Integer)
    w_1stWon=Column(Integer)
    w_2ndWon=Column(Integer)
    w_SvGms=Column(Integer)
    w_bpSaved=Column(Integer)
    w_bpFaced=Column(Integer)
    l_ace=Column(Integer)
    l_df=Column(Integer)
    l_svpt=Column(Integer)
    l_1stIn=Column(Integer)
    l_1stWon=Column(Integer)
    l_2ndWon=Column(Integer)
    l_SvGms=Column(Integer)
    l_bpSaved=Column(Integer)
    l_bpFaced=Column(Integer)
    winner_rank=Column(Integer)
    winner_rank_points=Column(Integer)
    loser_rank=Column(Integer)
    loser_rank_points=Column(Integer)
    tourney_id=Column(String)
    
class AtpQuallChall(Base):
    __tablename__='atp_qualifiers_challengers_matches'

    match_id = Column(String, primary_key=True)
    match_num= Column(Integer)
    winner_id= Column(BigInteger,ForeignKey("atp_players.player_id"))
    winner_seed= Column(String)
    winner_entry=Column(String)
    winner_age=Column(BigInteger,default=False)
    loser_id=Column(BigInteger,ForeignKey("atp_players.player_id"))
    loser_seed=Column(String)
    loser_entry=Column(String)
    loser_age=Column(Float)
    score=Column(String)
    round=Column(String)
    minutes=Column(Integer)
    w_ace=Column(Integer)
    w_df=Column(Integer)
    w_svpt=Column(Integer)
    w_1stIn=Column(Integer)
    w_1stWon=Column(Integer)
    w_2ndWon=Column(Integer)
    w_SvGms=Column(Integer)
    w_bpSaved=Column(Integer)
    w_bpFaced=Column(Integer)
    l_ace=Column(Integer)
    l_df=Column(Integer)
    l_svpt=Column(Integer)
    l_1stIn=Column(Integer)
    l_1stWon=Column(Integer)
    l_2ndWon=Column(Integer)
    l_SvGms=Column(Integer)
    l_bpSaved=Column(Integer)
    l_bpFaced=Column(Integer)
    winner_rank=Column(Integer)
    winner_rank_points=Column(Integer)
    loser_rank=Column(Integer)
    loser_rank_points=Column(Integer)
    tourney_id=Column(String)
    
class AtpAmateurs(Base):
    __tablename__='atp_amateurs_matches'

    match_id = Column(String, primary_key=True)
    match_num= Column(Integer)
    winner_id= Column(BigInteger,ForeignKey("atp_players.player_id"))
    winner_seed= Column(String)
    winner_entry=Column(String)
    winner_age=Column(BigInteger,default=False)
    loser_id=Column(BigInteger,ForeignKey("atp_players.player_id"))
    loser_seed=Column(String)
    loser_entry=Column(String)
    loser_age=Column(Float)
    score=Column(String)
    round=Column(String)
    minutes=Column(Integer)
    w_ace=Column(Integer)
    w_df=Column(Integer)
    w_svpt=Column(Integer)
    w_1stIn=Column(Integer)
    w_1stWon=Column(Integer)
    w_2ndWon=Column(Integer)
    w_SvGms=Column(Integer)
    w_bpSaved=Column(Integer)
    w_bpFaced=Column(Integer)
    l_ace=Column(Integer)
    l_df=Column(Integer)
    l_svpt=Column(Integer)
    l_1stIn=Column(Integer)
    l_1stWon=Column(Integer)
    l_2ndWon=Column(Integer)
    l_SvGms=Column(Integer)
    l_bpSaved=Column(Integer)
    l_bpFaced=Column(Integer)
    winner_rank=Column(Integer)
    winner_rank_points=Column(Integer)
    loser_rank=Column(Integer)
    loser_rank_points=Column(Integer)
    tourney_id=Column(String)
    
class AtpDoubles(Base):
    __tablename__='atp_doubles_matches'

    match_id = Column(String, primary_key=True)
    match_num= Column(Integer)
    winner1_id= Column(BigInteger,ForeignKey("atp_players.player_id"))
    winner_seed= Column(String)
    winner_entry=Column(String)
    winner1_age=Column(BigInteger,default=False)
    winner2_id= Column(BigInteger,ForeignKey("atp_players.player_id"))
    winner2_age=Column(BigInteger,default=False)
    loser1_id=Column(BigInteger,ForeignKey("atp_players.player_id"))
    loser_seed=Column(String)
    loser_entry=Column(String)
    loser1_age=Column(Float)
    loser2_id=Column(BigInteger,ForeignKey("atp_players.player_id"))
    loser2_age=Column(Float)
    score=Column(String)
    round=Column(String)
    minutes=Column(Integer)
    w_ace=Column(Integer)
    w_df=Column(Integer)
    w_svpt=Column(Integer)
    w_1stIn=Column(Integer)
    w_1stWon=Column(Integer)
    w_2ndWon=Column(Integer)
    w_SvGms=Column(Integer)
    w_bpSaved=Column(Integer)
    w_bpFaced=Column(Integer)
    l_ace=Column(Integer)
    l_df=Column(Integer)
    l_svpt=Column(Integer)
    l_1stIn=Column(Integer)
    l_1stWon=Column(Integer)
    l_2ndWon=Column(Integer)
    l_SvGms=Column(Integer)
    l_bpSaved=Column(Integer)
    l_bpFaced=Column(Integer)
    winner1_rank=Column(Integer)
    winner1_rank_points=Column(Integer)
    winner2_rank=Column(Integer)
    winner2_rank_points=Column(Integer)
    loser1_rank=Column(Integer)
    loser1_rank_points=Column(Integer)
    loser2_rank=Column(Integer)
    loser2_rank_points=Column(Integer)    
    tourney_id=Column(String)
    
    
class AtpPlayers(Base):
    __tablename__='atp_players'
    
    player_id=Column(BigInteger,primary_key=True)
    name_first=Column(String)
    name_last=Column(String)
    hand=Column(String)
    dob=Column(Date)
    ioc=Column(String,ForeignKey("countries.alpha-3"))    
    height=Column(String)
    wikidata_id=Column(String)
    name_full=Column(String)
    
    
class AtpRanking(Base):
    __tablename__='atp_rankings'
    
    ranking_date=Column(Date)
    rank=Column(Integer)
    player=Column(BigInteger,ForeignKey("atp_players.player_id"))
    points=Column(Integer)
    ranking_id=Column(String,primary_key=True)
    
    
        
class WtaPlayers(Base):
    __tablename__='wta_players'
    
    player_id=Column(BigInteger,primary_key=True)
    name_first=Column(String)
    name_last=Column(String)
    hand=Column(String)
    dob=Column(Date)
    ioc=Column(String,ForeignKey("countries.alpha-3"))    
    height=Column(String)
    wikidata_id=Column(String)
    name_full=Column(String)
    
    
class WtaRanking(Base):
    __tablename__='wta_rankings'
    
    ranking_date=Column(Date)
    rank=Column(Integer)
    player=Column(BigInteger,ForeignKey("atp_players.player_id"))
    points=Column(Integer)
    tours=Column(Float)
    ranking_id=Column(String,primary_key=True)
    
    
class WtaSingles(Base):
    __tablename__='wta_singles_matches'

    match_id = Column(String, primary_key=True)
    match_num= Column(Integer)
    winner_id= Column(BigInteger,ForeignKey("atp_players.player_id"))
    winner_seed= Column(String)
    winner_entry=Column(String)
    winner_age=Column(BigInteger,default=False)
    loser_id=Column(BigInteger,ForeignKey("atp_players.player_id"))
    loser_seed=Column(String)
    loser_entry=Column(String)
    loser_age=Column(Float)
    score=Column(String)
    round=Column(String)
    minutes=Column(Integer)
    w_ace=Column(Integer)
    w_df=Column(Integer)
    w_svpt=Column(Integer)
    w_1stIn=Column(Integer)
    w_1stWon=Column(Integer)
    w_2ndWon=Column(Integer)
    w_SvGms=Column(Integer)
    w_bpSaved=Column(Integer)
    w_bpFaced=Column(Integer)
    l_ace=Column(Integer)
    l_df=Column(Integer)
    l_svpt=Column(Integer)
    l_1stIn=Column(Integer)
    l_1stWon=Column(Integer)
    l_2ndWon=Column(Integer)
    l_SvGms=Column(Integer)
    l_bpSaved=Column(Integer)
    l_bpFaced=Column(Integer)
    winner_rank=Column(Integer)
    winner_rank_points=Column(Integer)
    loser_rank=Column(Integer)
    loser_rank_points=Column(Integer)
    tourney_id=Column(String)
    
    
class WtaQualifiersItf(Base):
    __tablename__='wta_qualifiers_itf_matches'

    match_id = Column(String, primary_key=True)
    match_num= Column(Integer)
    winner_id= Column(BigInteger,ForeignKey("atp_players.player_id"))
    winner_seed= Column(String)
    winner_entry=Column(String)
    winner_age=Column(BigInteger,default=False)
    loser_id=Column(BigInteger,ForeignKey("atp_players.player_id"))
    loser_seed=Column(String)
    loser_entry=Column(String)
    loser_age=Column(Float)
    score=Column(String)
    round=Column(String)
    minutes=Column(Integer)
    w_ace=Column(Integer)
    w_df=Column(Integer)
    w_svpt=Column(Integer)
    w_1stIn=Column(Integer)
    w_1stWon=Column(Integer)
    w_2ndWon=Column(Integer)
    w_SvGms=Column(Integer)
    w_bpSaved=Column(Integer)
    w_bpFaced=Column(Integer)
    l_ace=Column(Integer)
    l_df=Column(Integer)
    l_svpt=Column(Integer)
    l_1stIn=Column(Integer)
    l_1stWon=Column(Integer)
    l_2ndWon=Column(Integer)
    l_SvGms=Column(Integer)
    l_bpSaved=Column(Integer)
    l_bpFaced=Column(Integer)
    winner_rank=Column(Integer)
    winner_rank_points=Column(Integer)
    loser_rank=Column(Integer)
    loser_rank_points=Column(Integer)
    tourney_id=Column(String)
    
    
class Countries(Base):
    __tablename__='countries'
    
    name=Column(String)
    alpha_2 = Column("alpha-2", String)
    alpha_3 = Column("alpha-3",String,primary_key=True)
    country_code=Column("country-code",Integer)
    iso_3166_2=Column("iso_3166-2",String)
    region=Column(String)
    sub_region=Column("sub-region",String)
    intermediate_region=Column("intermediate-region",String)
    region_code=Column("region-code",Integer)
    sub_region_code=Column("sub-region-code",Integer)
    intermediate_region_code=Column("intermediate-region-code",Integer)
    
    
class TotalTourneys(Base):
    __tablename__="total_tourneys"
    
    tourney_name=Column(String,primary_key=True)
    surface=Column(String)
    draw_size=Column(String)
    tourney_level=Column(String)
    tourney_date=Column(Date)
    tourney_name_date_matches=Column(String)
    best_of=Column(String)
    
    
class TemporalTable(Base):
    __tablename__="temporal_table"
    
    date = Column(Date, primary_key=True)
    
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    quarter = Column(Integer)
    month_name = Column(String)
    day_name = Column(String)
    week_of_year = Column(Integer)
    is_weekend = Column(Boolean)
    is_month_end = Column(Boolean)
    is_month_start = Column(Boolean)
    is_quarter_end = Column(Boolean)
    is_quarter_start = Column(Boolean)
    is_year_end = Column(Boolean)
    is_year_start = Column(Boolean)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    