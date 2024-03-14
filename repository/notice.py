import datetime

from sqlalchemy.orm import Session

from model.notice import Notice
from schema.notice import NoticeCreateItem

class NoticeRepository:
  def create(self, db: Session, notice: NoticeCreateItem):
    db_notice = Notice(
      num=notice.num,
      title=notice.title,
      href=notice.href,
      author=notice.author,
      noticeDate=notice.noticeDate,
      type=notice.type,
      source=notice.source
    )
    db.add(db_notice)
    db.commit()
    db.refresh(db_notice)
    return db_notice
  
  def select_list(self, db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notice).offset(skip).limit(limit).all()
  
  def select(self, db: Session, notice_id: int):
    result = db.query(Notice).filter(Notice.id == notice_id).first()
    return result
  
  def update(self, db: Session, notice_id: int, notice: NoticeCreateItem):
    db_notice = db.query(Notice).filter(Notice.id == notice_id).first()
    db_notice.num = notice.num
    db_notice.title = notice.title
    db_notice.href = notice.href
    db_notice.author = notice.author
    db_notice.noticeDate = notice.noticeDate
    db_notice.type = notice.type
    db_notice.source = notice.source
    db_notice.modDt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_notice.modUs = 'system'
    db.commit()
    db.refresh(db_notice)
    return db_notice