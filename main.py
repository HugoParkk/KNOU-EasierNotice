import requests
import copy
import time
import datetime
from bs4 import BeautifulSoup as BS

from dbConnect import DbConnect
from notice import Notice


conn = DbConnect()

noticeType = {
    "school": "SCHOOL",
    "regional_school": "REGIONAL",
    "department": "DEPARTMENT",
}

sources = {
    "school": {
        "knou": "knou",
    },
    "regional_school": {
        "seoul": "2141",
        "busan": "2142",
    },
    "department": {
        "cs": ["cs1", "4812"],
    },
}


def select_last_notice(source):
    try:
        sql = """
        SELECT IFNULL(max(num), 0)
        FROM notice
        WHERE source = '{source}'
        """.format(
            source=source
        )

        # print("sql: ", sql)

        result = conn.selectOne(sql)
        return result

    except Exception as e:
        print("select_last_notice error: ", e)
        print(e.with_traceback)
        return False


def insert_query(notice: Notice):
    try:
        sql = """
        INSERT 
        INTO notice 
        (num, title, href, author, noticeDate, insDt, modDt, type, source) 
        VALUES ('{num}', '{title}', '{href}', '{author}', '{noticeDate}', '{insDt}', '{modDt}', '{type}', '{source}')
        """.format(
            num=notice.num,
            title=notice.title,
            href=notice.href,
            author=notice.author,
            noticeDate=notice.noticeDate,
            insDt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            modDt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            type=notice.type,
            source=notice.source,
        )

        # print("sql: ", sql)

        conn.insert(sql)

    except Exception as e:
        print("insert_query error: ", e)
        print(e.with_traceback())
        return False

    return True


def get_notice_school():
    print()
    print("=====================================")
    print("방통대 공지사항")
    print()
    req = requests.get("https://www.knou.ac.kr/knou/561/subview.do?epTicket=LOG")
    html = req.text
    soup = BS(html, "html.parser").find("tbody")

    notices = soup.find_all("tr", {"class": ""})
    notices.sort(
        key=lambda x: x.find("td", {"class": "td-subject"})
        .find("a")
        .get("href")
        .split("/")[4],
        reverse=True,
    )
    print("notices length: ", len(notices))

    maxNoticeNum: int = int(
        notices[0]
        .find("td", {"class": "td-subject"})
        .find("a")
        .get("href")
        .split("/")[4]
    )
    lastNoticeNum: int = select_last_notice(sources["school"]["knou"])

    if lastNoticeNum >= maxNoticeNum:
        print("최신 공지사항입니다.")
        return

    for notice in notices:
        num = notice.find("td", {"class": "td-num"}).text
        href = notice.find("td", {"class": "td-subject"}).find("a").get("href")
        hrefNum: int = int(href.split("/")[4])
        title = notice.find("td", {"class": "td-subject"}).find("strong").text
        author = notice.find("td", {"class": "td-write"}).text.strip()
        noticeDate = notice.find("td", {"class": "td-date"}).text
        
        if hrefNum > lastNoticeNum:
          print("Title: ", title)
          print("Num: ", num)
          print("href: ", href)
          print("hrefNum: ", hrefNum)
          print("author: ", author)
          print("noticeDate: ", noticeDate)
          print("")
          print("")
          notice = Notice(
              title,
              hrefNum,
              href,
              author,
              noticeDate,
              noticeType["school"],
              sources["school"]["knou"],
          )
          print("notice: ", notice)
          if insert_query(notice):
              print("insert_query success")
          else:
              print("insert_query fail")


def get_notice_regional_school(region):
    print()
    print("=====================================")
    print("방통대 지역대학 공지사항")
    print()
    req = requests.get(
        "https://www.knou.ac.kr/regional/2479/subview.do?bbsClSeq={region}&epTicket=LOG".format(
            region=region
        )
    )
    html = req.text
    soup = BS(html, "html.parser").find("tbody")

    notices = soup.find_all("tr", {"class": ""})
    notices.sort(key=lambda x: x.find("td", {"class": "td-num"}).text, reverse=True)
    print("notices length: ", len(notices))
    maxNoticeNum: int = int(notices[0].find("td", {"class": "td-num"}).text)
    lastNoticeNum: int = select_last_notice(region)

    if lastNoticeNum >= maxNoticeNum:
        print("최신 공지사항입니다.")
        return

    for notice in notices:
        num = notice.find("td", {"class": "td-num"}).text
        href = notice.find("td", {"class": "td-subject"}).find("a").get("href")
        hrefNum = int(href.split("/")[4])
        title = notice.find("td", {"class": "td-subject"}).find("strong").text
        author = notice.find("td", {"class": "td-write"}).text.strip()
        noticeDate = notice.find("td", {"class": "td-date"}).text

        if hrefNum > lastNoticeNum:
          print("Title: ", title)
          print("Num: ", num)
          print("href: ", href)
          print("hrefNum: ", hrefNum)
          print("author: ", author)
          print("noticeDate: ", noticeDate)
          print("")
          print("")
          notice = Notice(
              title,
              hrefNum,
              href,
              author,
              noticeDate,
              noticeType["regional_school"],
              region,
          )
          if insert_query(notice):
              print("insert_query success")
          else:
              print("insert_query fail")


def get_notice_department(department):
    print()
    print("=====================================")
    print("방통대 학과 공지사항")
    print()
    req = requests.get(
        "https://www.knou.ac.kr/{departmentName}/{departmentNum}/subview.do?epTicket=LOG".format(
            departmentName=department[0], departmentNum=department[1]
        )
    )
    html = req.text
    soup = BS(html, "html.parser").find("tbody")

    notices = soup.find_all("tr", {"class": ""})
    notices.sort(key=lambda x: x.find("td", {"class": "td-num"}).text, reverse=True)
    print("notices length: ", len(notices))

    maxNoticeNum: int = int(notices[0].find("td", {"class": "td-num"}).text)
    lastNoticeNum: int = select_last_notice(department[0])

    if lastNoticeNum >= maxNoticeNum:
        print("최신 공지사항입니다.")
        return

    for notice in notices:
        num = notice.find("td", {"class": "td-num"}).text
        href = notice.find("td", {"class": "td-subject"}).find("a").get("href")
        hrefNum = int(href.split("/")[4])
        title = notice.find("td", {"class": "td-subject"}).find("strong").text
        author = notice.find("td", {"class": "td-write"}).text.strip()
        noticeDate = notice.find("td", {"class": "td-date"}).text

        if hrefNum > lastNoticeNum:
          print("Title: ", title)
          print("Num: ", num)
          print("href: ", href)
          print("hrefNum: ", hrefNum)
          print("author: ", author)
          print("noticeDate: ", noticeDate)
          print("")
          print("")
          notice = Notice(
              title,
              num,
              href,
              author,
              noticeDate,
              noticeType["department"],
              department[0],
          )
          if insert_query(notice):
              print("insert_query success")
          else:
              print("insert_query fail")


if __name__ == "__main__":
    print("Hello, World!")

    try:
        print("방통대 공지사항 모아보기 크롤러")
        print("")
        print("")

        while True:
            get_notice_school()  # 방통대 공지사항
            get_notice_regional_school(
                sources["regional_school"]["seoul"]
            )  # 방통대 지역대학 공지사항
            get_notice_department(sources["department"]["cs"])  # 방통대 학과 공지사항

            print()
            print("=====================================")
            print()
            print()
            print("END")
            print()
            print()
            time.sleep(1200)
    except Exception as e:
        print("크롤러를 실행하는데 문제가 발생했습니다.")
        print(e)
        print(e.with_traceback)
        print("크롤러를 종료합니다.")
        conn.closeConn()
        exit(1)
