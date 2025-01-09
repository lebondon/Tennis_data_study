from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey

class Singles(Base):
    __tablename__='atp_singles_matches'

    id = Column(Integer,primary_key=True,index=True)
    title= Column(String)
    description= Column(String)
    priority=Column(String)
    complete=Column(Boolean,default=False)