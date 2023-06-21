from schemas.schema import ItemCreate
from db.engine import SessionLocal
from models.model import Item
from sqlalchemy.exc import SQLAlchemyError

def create_item(item_data):
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