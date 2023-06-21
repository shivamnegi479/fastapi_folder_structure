from fastapi import APIRouter
from db.engine import SessionLocal
from models.model import Item
from schemas.schema import ItemCreate
from sqlalchemy.exc import SQLAlchemyError
from db.to_db import create_item

users = APIRouter()


@users.post("/items/")
async def post_item(item_data: ItemCreate):
    return create_item(item_data)