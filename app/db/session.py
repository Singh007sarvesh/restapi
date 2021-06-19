from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from app.core import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, 
	pool_size=20, max_overflow=100)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
db = Session()
# try:
	# db = Session()
# finally:
	# db.close()