# 텍스트기반 파일 다운로드하기 -------------------------
# 라이브러리 로딩
import urllib.request

# 데이터 변수 선언
URL = 'http://api.aoikujira.com/ip/ini'

# WEB 데이터 가져오기
res = urllib.request.urlopen(URL)
data = res.read()

# 바이트 데이터 읽고 확인 -------------------------------
print('type(data) =', type(data))      # 타입 체크
print(data)

# 바이트 데이터 => 문자열 변환 모니터에 출력
text = data.decode("utf-8")
print('\ntype(text) =', type(text))      # 타입 체크
print(text)

# 문자열 데이터 => 컴퓨터가 이해하도록 인코딩하여 저장
with open('../Data/web_data.txt', mode='wb') as file:
    file.write(text.encode("utf-8"))

# TXT 파일 읽기 ---------------------------------
with open('../Data/web_data.txt', mode='rb') as file:
    print(file.read().decode('utf-8'))

