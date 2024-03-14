import datetime

from sqlalchemy import Column, String, Integer, DateTime, Date
from config.database import Base

class Notice(Base):
  __tablename__ = 'notice'

  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  num = Column(Integer, primary_key=True)
  title = Column(String)
  href = Column(String)
  author = Column(String, nullable=True)
  noticeDate = Column(Date)
  insDt = Column(DateTime, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
  modDt = Column(DateTime, nullable=True, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
  insUs = Column(String, nullable=True, default='system') 
  modUs = Column(String, nullable=True, default='system')
  type = Column(String, nullable=True)
  source = Column(String, nullable=True)