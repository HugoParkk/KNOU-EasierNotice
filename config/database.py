import yaml
import pymysql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


with open('application-secret.yaml', 'r') as f:
  dbConfig = yaml.safe_load(f)

  userName = dbConfig['db']['userName']
  password = dbConfig['db']['password']
  host = dbConfig['db']['host']
  port = dbConfig['db']['port']
  dbName = dbConfig['db']['dbName']


  dbUrl = f"mysql+pymysql://{userName}:{password}@{host}:{port}/{dbName}?charset=utf8"
  print()
  print(dbUrl)
  print()
  engine = create_engine(dbUrl, echo=True)
  # engine.connect().exec_driver_sql("SELECT IFNULL(max(num), 0) FROM notice")
  SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

# conn = pymysql.connect(host=host, port=port, user=userName, password=password, db=dbName, charset='utf8')


  # def selectAll(self, sql):
  #   with conn.cursor() as cursor:
  #     cursor.execute(sql)
  #     result = cursor.fetchall()
  #     return result
  
  # def selectOne(self, sql):
  #   with conn.cursor() as cursor:
  #     cursor.execute(sql)
  #     result = cursor.fetchone()
  #     return result[0]
    
  # def insert(self, sql):
  #   with conn.cursor() as cursor:
  #     cursor.execute(sql)
  #   conn.commit()
  #   return cursor.lastrowid
  
  # def update(self, sql):
  #   with conn.cursor() as cursor:
  #     cursor.execute(sql)
  #   conn.commit()
  #   return cursor.rowcount
  
  # def delete(self, sql):
  #   with self.conn.cursor() as cursor:
  #     cursor.execute(sql)
  #   self.conn.commit()
  #   return cursor.rowcount
