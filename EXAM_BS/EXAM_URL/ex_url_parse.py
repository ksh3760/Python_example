# -------------------------------------------------------
# URL을 6개의 구성요소로 구분
# -------------------------------------------------------
# 라이브러리 로딩
from urllib.parse import urlparse      # 함수만 포함


# 분석하고 싶은 URL 지정
componets = urlparse('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98')

print(f'url componets => {type(componets)}, {componets}')
print(f'componets.scheme = {componets.scheme}')
print(f'componets.netloc = {componets.netloc}')
print(f'componets.path = {componets.path}')
print(f'componets.params = {componets.params}')
print(f'componets.query = {componets.query}')
print(f'componets.fragment = {componets.fragment}')
