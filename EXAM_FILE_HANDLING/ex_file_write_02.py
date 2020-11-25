# --------------------------------------------
# File Write 실습 02
# --------------------------------------------
if 0:
    # 키보드로 입력 받은 메세지를 파일에 기록
    # 'q' 입력 시 종료
    # ----------------------------------------------------------------------------
    import time as t    # 입력받은 시간 기록을 위한 time 모듈 불러오기

    try:
        file = open('FileWrite실습02.txt', mode='w', encoding='utf-8')

        while True:
            x = input("텍스트를 입력하세요 : ")
            setTime = t.ctime(t.time()) + " : " # 변수 setTime에 시간 저장

            if x == 'q': break
            file.write(setTime + x + '\n')

        file.close()

    except Exception as e:
        print(f"ERROR : {e}")

if 0:
    # home.html -> home.txt로 저장

    R_FILE = './DATA/home.html'
    W_FILE = './DATA/home.txt'
    DATA = ''

    try:
        # 1) 파일 읽기
        with open(R_FILE, mode='r', encoding='utf-8') as rfile:
            DATA = rfile.read()

        # 2) 파일 쓰기
        with open(W_FILE, mode='w', encoding='utf-8') as wfile:
            wfile.write(DATA)

    except Exception as e:
        print(f"ERROR : {e}")

if 1:
    # 10 byte로 읽어오기

    # R_FILE = './DATA/home.html'
    # W_FILE = './DATA/home.txt'
    DATA_SIZE = 10

    try:
        # 1) 파일 읽기
        with open(R_FILE, mode='r', encoding='utf-8') as rfile:
            # 2) 파일 쓰기
            with open(W_FILE, mode='w', encoding='utf-8') as wfile:
                while True:
                    DATA = rfile.read(DATA_SIZE)
                    if not DATA: break
                    wfile.write(DATA)

    except Exception as e:
        print(f"ERROR : {e}")
