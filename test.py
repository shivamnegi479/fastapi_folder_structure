from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus
ps=quote_plus('26547234s@S')
app = FastAPI()

# Database Connection
db_uri =  f"postgresql://postgres:{ps}@localhost/ecb"
# Replace 'username', 'password', 'host', 'port', and 'database' with your MySQL credentials

engine = create_engine(db_uri, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(255))


Base.metadata.create_all(bind=engine)


class ItemCreate(BaseModel):
    name: str
    description: str


@app.post("/items/")
async def create_item(item_data: ItemCreate):
    try:
        db = SessionLocal()
        item = Item(name=item_data.name, description=item_data.description)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    except SQLAlchemyError as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="test:app", host="localhost", reload=True)
