# 이미지 파일 다운로드하기 ------------------------------------------
import urllib.request
import os

# URL과 저장 경로 지정
URL = "https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
SAVE_DIR="../Data/"
SAVE_FILE = "../Data/google.png"

# 폴더가 없는 경우 생성
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# 파일 형태로 다운로드
urllib.request.urlretrieve( URL, SAVE_FILE )

print("저장되었습니다...!")
