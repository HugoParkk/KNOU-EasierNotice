from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from config.database import get_db
from model.notice import Notice
from schema.notice import NoticeCreateItem, NoticeSelectItem
from repository.notice import NoticeRepository

router = APIRouter(
  prefix="/notice",
  tags=["notice"],
)

@router.get("/", response_model=List[NoticeSelectItem])
def get_notice_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
  return NoticeRepository().select_list(db, skip, limit)

@router.get("/{notice_id}", response_model=NoticeSelectItem)
def get_notice(notice_id: int, db: Session = Depends(get_db)):
  db_notice = NoticeRepository().select(db, notice_id)
  if db_notice is None:
    raise HTTPException(status_code=404, detail="Notice not found")
  return db_notice