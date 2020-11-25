# -----------------------------------
# CSV 파일 읽기 & 쓰기 실습
# CSV 표준 라이브러리 사용
# -----------------------------------
import csv

# CSV 파일 생성 -----------------------
with open('./DATA/mytest.csv', mode='w', encoding='utf-8', newline='') as fp:
    # CSV 쓰기객체(writer) 생성
    writer = csv.writer(fp, delimiter='\t', quotechar='"')

    # 1줄씩 쓰기
    writer.writerow(['ID', 'NAME', 'PRICE'])
    writer.writerow(['S001', 'SD카드', 10000])

# CSV 파일 읽기 -------------------------
with open('./DATA/mytest.csv', mode='r', encoding='utf-8', newline='') as fp:
    # CSV 읽기객체(reader)생성
    reader = csv.reader(fp, delimiter='\t')

    # csv 데이터 출력하기
    for line in reader:
        print(f"Line => {line}")
