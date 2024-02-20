class Notice:
  def __init__(self, title, num, href, author, noticeDate):
    self.title = title
    self.num = num
    self.href = href
    self.author = author
    self.noticeDate = noticeDate

  def __str__(self):
    return 'title: {title}, num: {num}, href: {href}, author: {author}, noticeDate: {noticeDate}'.format(title=self.title, num=self.num, href=self.href, author=self.author, noticeDate=self.noticeDate)
  