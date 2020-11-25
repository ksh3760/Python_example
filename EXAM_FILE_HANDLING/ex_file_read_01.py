# ----------------------------------
# File 읽기 실습
# ----------------------------------
if 0:
    # 파일 읽어서 전체 문자열 데이터 가져오기
    file = open('test01.txt', mode='r', encoding='utf-8')
    alldata = file.read()

    print(f"All Data = {alldata}")
    file.close()

if 0:
    # 파일에서 지정된 갯수만큼 읽어오기
    file = open('test01.txt', mode='r', encoding='utf-8')
    data = file.read(10)
    print(f"data => {len(data)} : {data}")
    file.close()

if 0:
    # 한 번 읽을 때 10개씩 읽고 전체 내용 출력하기
    file = open('test01.txt', mode='r', encoding='utf-8')
    while True:
        data = file.read(10)
        if not data: break
        print(f"data => {len(data)} : {data}")

    file.close()

if 0:
    # 파일의 문자열 데이터 1줄 일기
    file = open('test01.txt', mode='r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line: break
       # line = line.strip("\n")

       # print(f"line = {file.readline()}")
       # print(f"line = {line} : {file.tell()}")
        print(f"line = {line}")
    file.close()

if 0:
    # 파일의 문자열 데이터를 줄단위로 전체 가져오기
    file = open('test01.txt', mode='r', encoding='utf-8')
    lines = file.readlines()
    print(f"lines DATA = {lines}")
    file.close()


if 1:
    # with ~ as 구문으로 처리하기
    try:
        with open('test01.txt', mode='r', encoding='utf-8') as file:
            lineData = file.readlines()
            print(f'lineData => {lineData}')

    except Exception as e:
        pass