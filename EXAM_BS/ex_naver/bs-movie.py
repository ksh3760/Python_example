# 네이버 영화로 부터 영화 정보 추출하기
# 라이브러리 로딩 -----------------------------
from bs4 import BeautifulSoup
import urllib.request as req

# 데이터 변수 선언 ------------------------------------
url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"

# 데이터 가져오기 urlopen() ----------------------------
res = req.urlopen(url)
print(type(res))

# 데이터 분석하기 -------------------------------------
soup = BeautifulSoup(res, "html.parser")

# 원하는 데이터 추출 ---------------------------------
# 1개 추출
# old_content > table > tbody > tr:nth-child(2) > td.title > div > a
movie = soup.select_one("#old_content > table > tbody > tr:nth-child(2) > td.title > div > a")
print("movie = ", movie.attrs['title'])  # 타이틀 속성 추출
print("movie = ", movie.string)

# 여러개 추출
# old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# old_content > table > tbody > tr:nth-child(3) > td.title > div > a
movies = soup.select("#old_content > table > tbody > tr > td.title > div > a")
print("len={}\nmovies = {}".format(len(movies), movies))

# 탑10 영화 리스트 출력
print('===== [영화 탑 10] =====')
num = 1
for movie in movies:  # movies를 사용하여 이터러블 데이터 추출
    print(f"{num} - {movie.string}")
    if num >= 10: break
    num += 1
