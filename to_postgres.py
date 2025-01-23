import polars as pl
from sqlalchemy import create_engine
import psycopg2
from utils.utils import *

#loads_parquets_to_postgres per mettere i parquet nel tuo server locale postgres (guarda la funzione su util.py per più dettagli)

#load_parquets_to_postgres()

#queste funzioni caricano i file su supabase, stavolta ogni file è diviso e non vengono caricati tutti insieme

#atp

#load_parquet_to_supabase('aggregated_matches_atp/atp_players.parquet', 'atp_players')
#load_parquet_to_supabase('aggregated_matches_atp/atp_singles_matches.parquet', 'atp_singles_matches')
#load_parquet_to_supabase('aggregated_matches_atp/atp_rankings.parquet', 'atp_rankings')
#load_parquet_to_supabase('aggregated_matches_atp/atp_qualifiers_challengers_matches.parquet', 'atp_qual_chall_matches')
#load_parquet_to_supabase('aggregated_matches_atp/atp_futures_matches.parquet', 'atp_futures_matches')
#load_parquet_to_supabase('aggregated_matches_atp/atp_doubles_matches.parquet', 'atp_doubles_matches')
#load_parquet_to_supabase('aggregated_matches_atp/atp_amateurs_matches.parquet', 'atp_amateurs_matches')

#wta

#load_parquet_to_supabase('aggregated_matches_wta/wta_qualifiers_itf_matches.parquet', 'wta_qual_itf_matches')
#load_parquet_to_supabase('aggregated_matches_wta/wta_rankings.parquet', 'wta_rankings')
#load_parquet_to_supabase('aggregated_matches_wta/wta_players.parquet', 'wta_players')
#load_parquet_to_supabase('aggregated_matches_wta/wta_singles_matches.parquet', 'wta_singles_matches')

#local
#load_parquets_to_postgres_local()

#tembo

#load_parquet_to_tembo('aggregated_matches_atp/atp_players.parquet', 'atp_players')
#load_parquet_to_tembo('aggregated_matches_atp/atp_singles_matches.parquet', 'atp_singles_matches')
#load_parquet_to_tembo('aggregated_matches_atp/atp_rankings.parquet', 'atp_rankings')
#load_parquet_to_tembo('aggregated_matches_atp/atp_qualifiers_challengers_matches.parquet', 'atp_qual_chall_matches')
#load_parquet_to_tembo('aggregated_matches_atp/atp_futures_matches.parquet', 'atp_futures_matches')
#load_parquet_to_tembo('aggregated_matches_atp/atp_doubles_matches.parquet', 'atp_doubles_matches')
#load_parquet_to_tembo('aggregated_matches_atp/atp_amateurs_matches.parquet', 'atp_amateurs_matches')

#load_parquet_to_tembo('aggregated_matches_wta/wta_qualifiers_itf_matches.parquet', 'wta_qual_itf_matches')
#load_parquet_to_tembo('aggregated_matches_wta/wta_rankings.parquet', 'wta_rankings')
#load_parquet_to_tembo('aggregated_matches_wta/wta_players.parquet', 'wta_players')
#load_parquet_to_tembo('aggregated_matches_wta/wta_singles_matches.parquet', 'wta_singles_matches')


#AWS test
