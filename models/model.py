from sqlalchemy import Column, Integer, String
from db.engine import Base,engine


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(255))

Base.metadata.create_all(bind=engine)

