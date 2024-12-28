import os
import polars as pl
from sqlalchemy import create_engine

def import_tennis_matches(base_path="matches_and_ranking_atp", data_type="singles",gender="atp",write_parquet=False):
    dataframes = []
    null_values = ['NA', 'N/A', '', '-', 'Unknown', 'null','�']
   
    # Define file prefixes for different match types
    match_types = {
        "singles": f"{gender}_matches",
        "doubles": f"{gender}_matches_doubles",
        "qualifiers_challengers": f"{gender}_matches_qual_chall",
        "futures": f"{gender}_matches_futures",
        "qualifiers_itf": f"{gender}_matches_qual_itf",
    }
   
    # Define year ranges for different match types
    year_ranges = {
        "singles": (1968, 2025),
        "doubles": (1968, 2025),
        "qualifiers_challengers": (1978, 2025),
        "futures": (1991, 2025),
        "qualifiers_itf": (1968, 2025),
    }
    
    if gender=="wta":
        base_path="matches_and_ranking_wta"
   
    # Get the appropriate prefixes and year range
    prefix = match_types.get(data_type)
    start_year, end_year = year_ranges.get(data_type)
   
    # Iterate through all specified prefixes
    for year in range(start_year, end_year):
        filename = f"{prefix}_{year}.csv"
        filepath = os.path.join(base_path, filename)
           
        if os.path.exists(filepath):
            try:
                    # Expanded schema overrides to preserve string types
                schema_overrides = {
                                    'tourney': pl.Utf8,
                                    'winner_seed': pl.Utf8,
                                    'winner_entry': pl.Utf8,
                                    'loser_seed': pl.Utf8,
                                    'loser_entry': pl.Utf8,
                                    'winner_rank': pl.Utf8,
                                    'winner_rank_points': pl.Utf8,
                                    'loser_rank': pl.Utf8,
                                    'loser_rank_points': pl.Utf8,
                                    'tourney_date': pl.Utf8,
                                    # Handle both singles and doubles ID fields
                                    'winner_id': pl.Utf8,
                                    'winner1_id': pl.Utf8,
                                    'winner2_id': pl.Utf8,
                                    'loser_id': pl.Utf8,
                                    'loser1_id': pl.Utf8,
                                    'loser2_id': pl.Utf8,
                                    # Handle both singles and doubles name fields
                                    'winner_name': pl.Utf8,
                                    'winner1_name': pl.Utf8,
                                    'winner2_name': pl.Utf8,
                                    'loser_name': pl.Utf8,
                                    'loser1_name': pl.Utf8,
                                    'loser2_name': pl.Utf8,
                                    # Handle both singles and doubles hand fields
                                    'winner_hand': pl.Utf8,
                                    'winner1_hand': pl.Utf8,
                                    'winner2_hand': pl.Utf8,
                                    'loser_hand': pl.Utf8,
                                    'loser1_hand': pl.Utf8,
                                    'loser2_hand': pl.Utf8
                                    }
                   
                df = pl.read_csv(
                                filepath,
                                schema_overrides=schema_overrides,
                                ignore_errors=False,
                                null_values=null_values,
                                infer_schema_length=50000,
                                try_parse_dates=True,
                                truncate_ragged_lines=True
                                )
                   
                    # Convert tourney_date to Date type
                df = df.with_columns(
                                    pl.col('tourney_date')
                                    .str.to_date(format='%Y%m%d')
                                    .alias('tourney_date')
                                    )
                
                dataframes.append(df)
                
            except Exception as e:
                    print(f"Error importing {filename}: {e}")
   
    # Vertical concat with relaxed schema
    matches=pl.concat(dataframes, how="vertical_relaxed")
    if write_parquet==True:
        matches.write_parquet(file=f"aggregated_matches_{gender}/{gender}_{data_type}_matches.parquet",compression="zstd")
    return matches



def import_players(base_path="matches_and_ranking_atp",gender="atp",write_parquet=False):
    
    if gender=="wta":
        base_path="matches_and_ranking_wta"
    players=pl.read_csv(f"{base_path}/{gender}_players.csv")
    players = players.with_columns(
    pl.concat_str(["name_first", "name_last"], separator=" ").alias("name_full")
    )

    players = players.with_columns(pl.col('dob').cast(pl.String, strict=False).alias('dob'))

    players = players.with_columns(
                    pl.col('dob')
                    .str.to_date(format='%Y%m%d',strict=False)
                    .alias('dob')
                    )
    if write_parquet==True:
        players.write_parquet(file=f"aggregated_matches_{gender}/{gender}_players.parquet",compression="zstd")
    return players



def import_matches_amateurs_atp(base_path="matches_and_ranking_atp",write_parquet=False):
    
    null_values = ['NA', 'N/A', '', '-', 'Unknown', 'null']
    schema_overrides = {
                        'winner_seed': pl.Utf8,
                        'loser_seed': pl.Utf8,
                        'tourney_date': pl.Utf8,
                        'winner_entry': pl.Utf8,
                        'loser_entry': pl.Utf8,
                        'winner_rank': pl.Utf8,
                        'loser_rank': pl.Utf8,
                        'winner1_id': pl.Utf8,
                        'winner2_id': pl.Utf8,
                        'loser1_id': pl.Utf8,
                        'loser2_id': pl.Utf8
                    }
                   
    amateur_matches = pl.read_csv(
                        source=f"{base_path}/atp_matches_amateur.csv",
                        schema_overrides=schema_overrides,
                        null_values=null_values,
                        infer_schema_length=10000
                    )
                   
                    # Convert tourney_date to Date type
    amateur_matches = amateur_matches.with_columns(
                    pl.col('tourney_date')
                    .str.to_date(format='%Y%m%d')
                    .alias('tourney_date')
                    )
    
    if write_parquet==True:
        amateur_matches.write_parquet(file='aggregated_matches_atp/atp_amateurs_matches.parquet',compression="zstd") 
        
    return amateur_matches



def import_rankings(base_path="matches_and_ranking_atp",gender="atp",write_parquet=False):
    
    dataframes=[]
    if gender=="wta":
        base_path="matches_and_ranking_wta"
        
    years=["70s","80s","90s","00s","10s","20s","current"]
    
    if gender=="wta":
       years=["80s","90s","00s","10s","20s","current"]
   
    for year in years:
        filename = f"{gender}_rankings_{year}.csv"
        filepath = os.path.join(base_path, filename)
           
        if os.path.exists(filepath):
            try:              
                if gender=="atp":
                    schema ={
                            "ranking_date": pl.Utf8,  # Keep as string initially
                            "rank": pl.Int64,
                            "player": pl.Utf8,
                            "points": pl.Int64
                            }
                else:
                    schema ={
                            "ranking_date": pl.Utf8,  # Keep as string initially
                            "rank": pl.Int64,
                            "player": pl.Utf8,
                            "points": pl.Int64,
                            "tours": pl.Int64
                            }
                
                # Read CSV with initial schema
                df = pl.read_csv(filepath, schema=schema)
                
                # Convert ranking_date to proper datetime
                df = df.with_columns(
                    pl.col("ranking_date").str.strptime(pl.Date, format="%Y%m%d")
                )
                
                dataframes.append(df)
                
            except Exception as e:
                    print(f"Error importing {filename}: {e}")
                    
        rankings=pl.concat(dataframes, how="vertical_relaxed")
    if write_parquet==True:
        rankings.write_parquet(file=f"aggregated_matches_{gender}/{gender}_rankings.parquet",compression="zstd")
    return rankings


def load_parquets_to_postgres():
    tables_names_atp=["atp_singles_matches","atp_doubles_matches","atp_amateurs_matches","atp_futures_matches","atp_qualifiers_challengers_matches","atp_rankings","atp_players"]
    tables_names_wta=["wta_singles_matches","wta_players","wta_rankings","wta_qualifiers_itf_matches"]
    
    engine = create_engine('postgresql://postgres:don@localhost:5432/tennis_stats')
    
    base_path="aggregated_matches_atp"
    
    for table in tables_names_atp:
        filename = table+".parquet"
        filepath = os.path.join(base_path, filename)
        df=pl.read_parquet(filepath)
        df.write_database(
                           table,
                           connection=engine,
                           if_table_exists="replace"
                         )
    
    base_path="aggregated_matches_wta"
    
    for table in tables_names_wta:
        filename = table+".parquet"
        filepath = os.path.join(base_path, filename)
        df=pl.read_parquet(filepath)
        df.write_database(
                           table,
                           connection=engine,
                           if_table_exists="replace"
                         )       
        
