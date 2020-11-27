# --------------------------------------------------------
# 2020. 11. 25 Python Programming Self Test
# -------------------------------------------------------
# 파이썬 예제
if 0:
    # (1) 1~100사이 범위에서 짝수의 합을 반환하는 함수 만들기
    #     함  수  명 : evenSum
    #     매개  변수 : 없음
    #     반  환  값 : 합
    def evenSum() :
        sum = 0
        for i in range(1, 101, 1):
            if i % 2 == 0:
                sum += i

        return sum

    print(evenSum())

if 0:
    # (2) 입력 받은 구구단을 출력하는 프로그램 만들기
    #     입력 예 )  3
    #     결과 예 )  3 * 1 = 3    3 * 2 = 6    3 * 3 = 9
    #               3 * 4 = 12   3 * 5 = 15   3 * 6 = 18
    #               3 * 7 = 21   3 * 8 = 24   3 * 9 = 27
    xnum = int(input("정수를 입력하세요 : "))

    for i in range(1, 10):
        if i % 3 != 0:
            print(f"{xnum} * {i} = {xnum * i}\t", end='')
        else:
            print(f"{xnum} * {i} = {xnum * i}")

if 0:
    # (3) 가변인자를 입력받아서 더하기, 빼기, 곱하기, 최대값, 최소값 출력 함수 만들기
    #     함  수  명 : allFunc
    #     매개  변수 : 수치데이터 가변인자
    #     반  환  값 : 더하기, 빼기, 곱하기, 최대값, 최소값
    def allFunc(*params) :
        # 더하기
        add = 0
        for i in params:
            add += i

        # 빼기
        sub = 0
        for i in params:
            sub -= i

        # 곱하기
        mul = 1
        for i in params:
            mul *= i

        return add, sub, mul, max(params), min(params)

    print(allFunc(1, 2, 3, 4, 5))

if 0:
    # (4) 입력받은 문자열을 변환하는 함수 만들기
    #     함  수  명 : convertFunc
    #     매개  변수 : str데이터
    #     반  환  값 : 없음
    #     입  력  예 ) Good Luck
    #     실  행  예 ) gOOD lUCK
    #                 G*o*o*d* *L*u*c*K
    #                 'Good', 'Luck'
    def converFunc(param):
        for i in param:
            if ord('A') <= ord(i) <= ord('Z'):
                print(i.lower(), end='')
            elif ord('a') <= ord(i) <= ord('z'):
                print(i.upper(), end='')
            else:
                print(i, end='')
        print()
        for i in param:
            print(i, end='*')
        print()
        print(param.split())

    print(converFunc('Good Luck'))


if 0:
    # (5) 입력받은 점수에 따른 학점을 출력하세요.
    #     A+, A, B+, B, C+, C, D+, D, F
    x = int(input("점수를 입력하세요 : "))
    if  x >= 95:
        print('A+')
    elif 95 > x >= 90:
        print('A')
    elif 90 > x >= 85:
        print('B+')
    elif 85 > x >= 80:
        print('B')
    elif 80 > x >= 75:
        print('C+')
    elif 75 > x >= 70:
        print('C')
    elif 70 > x >= 65:
        print('D+')
    elif 65 > x >= 60:
        print('D')
    else:
        print("F")

if 0:
    # (6) 1~50사이 범위에서 소수를 출력하세요.
    #     소수(prime number): 1과 자기자신으로만 나누어지는 수
    #     값 : 2, 3, 5, 7, 11, 13, 17, 19, ......
    for i in range(2, 51):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i, end=', ')

if 0:
    # (7) 계산기 클래스를 만들기
    #     클래스 명 :  Calc
    #     메 서 드 :  더하기, 곱하기, 나누기, 빼기, 종합(4가지 연산 한꺼번에 수행)
    #     동    작 : 메서드는 결과값 반환
    class Calc:

        def calFunc(param, param1):
            add = param + param1
            mul = param * param1
            div = round(param / param1, 2)
            sub = param - param1

            return add, mul, div, sub

    print(Calc.calFunc(2, 3))

if 0:
    # (8) 10명에 대한 비만도 정보 저장 기능 만들기
    #     기    능 :  이름, 키, 몸무게 입력 받아서 BMI 계산
    #                - 이름, BMI 정보 저장
    #                - 이름으로 BMI에 따른 저체중, 정상, 비만 정보 출력

    # 함수생성
    def bmiFunc(w, h):  # bmi 계산
        # BMI지수 = 몸무게(kg) / (신장(m) * 신장(m))
        h = h / 100
        x = round(w / (h * h), 3)
        # 비만의 정도를 측정
        if x >= 35:
            return '고도비만', x
        elif x >= 30:
            return '중정도 비만', x
        elif x >= 25:
            return '경도 비만', x
        elif x >= 23:
            return '과체중', x
        elif x >= 18.5:
            return '정상체중', x
        else:
            return '저체중', x

    # 입력
    cnt = 0
    file = open('bmiInfo.txt', mode='w', encoding='utf-8')
    while cnt < 2:
        try:
            name = input("이름을 입력하세요 : ")
            height = int(input("키를 입력하세요 : "))
            weight = int(input("몸무게를 입력하세요 :"))
            bmi = bmiFunc(weight, height)
            file.write(f"{cnt+1}. {name} : {bmi}\n")
        except Exception as e:
            print("[예외발생. 다시해주세요]")
            print('--------------------------------')
        else:
            print("[정상적으로 입력 되었습니다.]")
            print('--------------------------------')
            cnt += 1

    file.close()  # 파일 닫기

    # 출력
    file = open('bmiInfo.txt', mode='r', encoding='utf-8')
    alldata = file.read()
    print('--------------------------------')
    print(f"{alldata}")
    print('--------------------------------')
    file.close()


if 0:
    # (9) CSV 파일 기록 및 읽기
    #     기    능 :  입력 받은 사람 정보( 이름, 성별, 나이, 지역) CSV 파일에 기록
    #     파 일 명 : person.csv
    import csv

    with open('../../Desktop/PycharmProjects/person.csv', mode='w', encoding='utf-8', newline='') as pf:
        w = csv.writer(pf, delimiter=',', quotechar='"')
        perInfo = input('이름, 성별, 나이, 지역을 입력하세요 : ').split()
        w.writerow(perInfo)

    # 출력
    with open('../../Desktop/PycharmProjects/person.csv', mode='r', encoding='utf-8', newline='') as pf:
        r = csv.reader(pf, delimiter='\t')
        for i in r:
            print(i)

if 0:
    # (10) 입력받은 메시지를 파일에 기록하고 확인하는 프로그램 만들기
    #     파일명 :  message.txt
    #     구  성 : 파일 기록 함수  + 파일 읽기 함수
    #     동  작 : write & read 중 사용자 선택
    #             write => 기록 함수 실행
    #             read  => 읽기 함수 실행
    import time as t

    # 파일기록 함수
    def write():
        file = open('../../Desktop/PycharmProjects/message.txt', mode='w', encoding='utf-8')
        msg = input("메세지를 입력하세요 : ")
        time = t.ctime() + " : "
        file.write(time + msg)
        file.close()

    # 파일읽기 함수
    def read():
        file = open('../../Desktop/PycharmProjects/message.txt', mode='r', encoding='utf-8')
        x = file.read()
        print(f"{x}")
        file.close()

    # 함수실행
    write()
    read()