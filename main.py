import requests
import copy
import time
from bs4 import BeautifulSoup as BS

def get_notice_school():
  req = requests.get(
        "https://www.knou.ac.kr/knou/561/subview.do?epTicket=LOG"
      )
  html = req.text
  soup = BS(html, "html.parser").find("tbody")
  checkList = []
  notices = soup.find_all("tr", {"class": ""})
  print('notices length: ', len(notices))
  for notice in notices:
    num = notice.find("td", {"class": "td-num"}).text
    href = notice.find("td", {"class": "td-subject"}).find("a").get("href")
    title = notice.find("td", {"class": "td-subject"}).find("strong").text
    author = notice.find("td", {"class": "td-write"}).text.strip()
    noticeDate = notice.find("td", {"class": "td-date"}).text
    checkList.append([num, title, author, noticeDate, href])
    print('Title: ', title)
    print('Num: ', num)
    print('href: ', href)
    print('author: ', author)
    print('noticeDate: ', noticeDate)
    print('')
    print('')


def get_notice_regional_school(region):
  req = requests.get(
        "https://www.knou.ac.kr/regional/2479/subview.do?bbsClSeq={region}&epTicket=LOG".format(region=region)
      )
  html = req.text
  soup = BS(html, "html.parser").find("tbody")
  checkList = []
  notices = soup.find_all("tr", {"class": ""})
  print('notices length: ', len(notices))
  for notice in notices:
    num = notice.find("td", {"class": "td-num"}).text
    href = notice.find("td", {"class": "td-subject"}).find("a").get("href")
    title = notice.find("td", {"class": "td-subject"}).find("strong").text
    author = notice.find("td", {"class": "td-write"}).text.strip()
    noticeDate = notice.find("td", {"class": "td-date"}).text
    checkList.append([num, title, author, noticeDate, href])
    print('Title: ', title)
    print('Num: ', num)
    print('href: ', href)
    print('author: ', author)
    print('noticeDate: ', noticeDate)
    print('')
    print('')


def get_notice_department(department):
  req = requests.get(
        # "https://www.knou.ac.kr/regional/2479/subview.do?bbsClSeq={department}&epTicket=LOG".format(department=department)
        "https://cs.knou.ac.kr/cs1/4812/subview.do?epTicket=LOG"
      )
  html = req.text
  soup = BS(html, "html.parser").find("tbody")
  checkList = []
  notices = soup.find_all("tr", {"class": ""})
  print('notices length: ', len(notices))
  for notice in notices:
    num = notice.find("td", {"class": "td-num"}).text
    href = notice.find("td", {"class": "td-subject"}).find("a").get("href")
    title = notice.find("td", {"class": "td-subject"}).find("strong").text
    author = notice.find("td", {"class": "td-write"}).text.strip()
    noticeDate = notice.find("td", {"class": "td-date"}).text
    checkList.append([num, title, author, noticeDate, href])
    print('Title: ', title)
    print('Num: ', num)
    print('href: ', href)
    print('author: ', author)
    print('noticeDate: ', noticeDate)
    print('')
    print('')


if __name__ == "__main__":
  print("Hello, World!")

  try:
    print("방통대 공지사항 모아보기 크롤러")
    print('')
    print('')


    while True:
      print('방통대 공지사항')
      get_notice_school() # 방통대 공지사항

      print('방통대 지역대학 공지사항')
      get_notice_regional_school('2141') # 방통대 지역대학 공지사항

      print('방통대 학과 공지사항')
      get_notice_department('cs1') # 방통대 학과 공지사항

      print('END')
      print('')
      print('')
      time.sleep(600)
  except Exception as e:
    print("크롤러를 실행하는데 문제가 발생했습니다.")
    print(e)
    print("크롤러를 종료합니다.")
    exit(1)


