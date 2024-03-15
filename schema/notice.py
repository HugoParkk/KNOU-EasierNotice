from pydantic import BaseModel, Field
import datetime

class NoticeCreateItem(BaseModel):
  num: int = Field(..., example=1)
  title: str = Field(..., example="title")
  href: str = Field(..., example="href")
  author: str = Field(..., example="author")
  noticeDate: str = Field(..., example="2024-01-01")
  type: str = Field(..., example="type")
  source: str = Field(..., example="source")

class NoticeSelectItem(BaseModel):
  id: int
  num: int
  title: str
  href: str
  author: str
  noticeDate: datetime.date
  type: str
  source: str

  class Config:
    orm_mode = True