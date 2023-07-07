from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
  
# Configure the PostgreSQL database connection
engine = create_engine("postgresql://postgres:sql21@localhost:5432/p2_sms")



db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
Base.metadata.bind = engine

# Initialize the database
def init_db():
    
    Base.metadata.create_all(bind=engine)