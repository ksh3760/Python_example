# 파이썬 이미지 크롤링 샘플 파일 입니다.
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


baseUrl = '이곳에 링크를 복사하여 붙여넣은 후 주석을 제거'
plusUrl = input('검색어를 입력하세요.')
url = baseUrl + quote_plus(plusUrl)

print(url)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')

#  print(img[0])

n = 1
for i in img:
   imgUrl = (i['data-source'])
   with urlopen(imgUrl) as f:
       with open('./img_test/' + plusUrl + str(n) + '.jpg', 'wb') as h:
           img = f.read()
           h.write(img)
           n += 1
           print(imgUrl)

print('Download complete')
