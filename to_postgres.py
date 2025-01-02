import polars as pl
from sqlalchemy import create_engine
import psycopg2
from utils.utils import *

#loads_parquets_to_postgres per mettere i parquet nel tuo server locale postgres (guarda la funzione su util.py per più dettagli)

load_parquets_to_postgres()
