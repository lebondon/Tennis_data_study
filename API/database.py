from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
#supabase

#DATABASE_URL=os.getenv("DATABASE_URL")

#engine = create_engine(DATABASE_URL)

#local

engine = create_engine('postgresql://postgres:don@localhost:5432/tennis_stats')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
