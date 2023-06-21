from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

ps = quote_plus('26547234s@S')

# Database Connection
db_uri = f"postgresql://postgres:{ps}@localhost/ecb"
# Replace 'username', 'password', 'host', 'port', and 'database' with your PostgreSQL credentials

engine = create_engine(db_uri, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
