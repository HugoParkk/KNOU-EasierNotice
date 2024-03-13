import yaml
import pymysql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class DbConnect:
  def __init__(self):
    with open('application-secret.yaml', 'r') as f:
      dbConfig = yaml.safe_load(f)

      self.userName = dbConfig['db']['userName']
      self.password = dbConfig['db']['password']
      self.host = dbConfig['db']['host']
      self.port = dbConfig['db']['port']
      self.dbName = dbConfig['db']['dbName']

      self.dbUrl = f"mysql+pymysql://{self.userName}:{self.password}@{self.host}:{self.port}/{self.dbName}?charset=utf8"

      self.engine = create_engine(self.dbUrl, echo=True)
      self.sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
      self.base = declarative_base()

      self.conn = pymysql.connect(host=self.host, port=self.port, user=self.userName, password=self.password, db=self.dbName, charset='utf8')

  def getConn(self):
    return self.conn
  
  def closeConn(self):
    self.conn.close()

  def __del__(self):
    self.closeConn()

  def selectAll(self, sql):
    with self.conn.cursor() as cursor:
      cursor.execute(sql)
      result = cursor.fetchall()
      return result
  
  def selectOne(self, sql):
    with self.conn.cursor() as cursor:
      cursor.execute(sql)
      result = cursor.fetchone()
      return result[0]
    
  def insert(self, sql):
    with self.conn.cursor() as cursor:
      cursor.execute(sql)
    self.conn.commit()
    return cursor.lastrowid
  
  def update(self, sql):
    with self.conn.cursor() as cursor:
      cursor.execute(sql)
    self.conn.commit()
    return cursor.rowcount
  
  def delete(self, sql):
    with self.conn.cursor() as cursor:
      cursor.execute(sql)
    self.conn.commit()
    return cursor.rowcount
