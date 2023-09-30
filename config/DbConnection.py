from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 연결할 db url

# class DbConnection:
#   def __init__(self):
#     SQLALCHEMY_DATABASE_URL = "mariadb://jachee:4eQJg8NWTCThBNHYR24NEEij3YVmxCc4@129.154.209.75:3306/prorank"
#     engine = create_engine(SQLALCHEMY_DATABASE_URL)
#     self.Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#     self.Base = declarative_base()
#
#   def getSession(self):
#     session = self.Session()
#     try:
#       yield session
#       session.commit()
#     except:
#       session.rollback()
#       raise
#     finally:
#       session.close()


SQLALCHEMY_DATABASE_URL = "mariadb://jachee:4eQJg8NWTCThBNHYR24NEEij3YVmxCc4@129.154.209.75:3306/prorank"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

@contextmanager
def session():
  session = Session()
  try:
    yield session
    session.commit()
  except:
    session.rollback()
    raise
  finally:
    session.close()