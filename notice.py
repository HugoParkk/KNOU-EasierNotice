class Notice:
  def __init__(self, title, num, href, author, noticeDate, type, source):
    self.title = title
    self.num = num
    self.href = href
    self.author = author
    self.noticeDate = noticeDate
    self.type = type
    self.source = source

  def __str__(self):
    return f"Notice({self.title}, {self.num}, {self.href}, {self.author}, {self.noticeDate}, {self.type}, {self.source})"
  