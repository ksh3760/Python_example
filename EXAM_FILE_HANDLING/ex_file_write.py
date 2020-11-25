# ----------------------------------------------
# File write 실습
# ----------------------------------------------
if 0:
    # 새 파일 생성 & 문자열 데이터 기록
    file = open('test01.txt', mode='w')  # 파일 생성('생성할 파일명', '쓰기')
    file.write("GOOD LUCK!\n")
    file.write("Happy New Year 2021")
    file.close()  # 파일 닫기


if 0:
    # 파일 존재 시 문자열 데이터 덧붙이기
    file = open('test01.txt', mode='a')
    file.write("\n-------------------")
    file.close()

if 0:
    # 메세지 10개 추가하기
    file = open('test02.txt', mode='a')
    for cnt in range(10):
        file.write(f"\n{cnt + 1} : Good Luck!")
    file.close()

if 0:
    # 여러개의 데이터 한꺼번에 기록 => list
    datas = ['오늘은 화요일입니다.\n', '12월이 코앞이네요\n', '겨울입니다.\n']

    # 파일 생성 & 데이터 기록
    file = open('messgae.txt', mode='w', encoding='utf-8')
    #file.writelines(datas)
    file.writelines('\n'.join(datas))
    file.close()

if 0:
    # 데이터 저장 폴더에 파일 저장하기
    #_폴더부터 생성#
    import os
    
    FILE_DIR = './DATA/'
    print(f'os.path.exists(FILE_DIR) => {os.path.exists(FILE_DIR)}')
    if not os.path.exists(FILE_DIR):
        os.makedirs(FILE_DIR)

    # 폴더 안에 파일 생성 및 데이터 기록
    file=open(FILE_DIR + 'data.txt', mode='w', encoding='utf-8')
    file.write('하하하하\n')
    file.close()

if 0:
    # 데이터 저장 폴더에 파일 저장하기
    # _폴더부터 생성#
    import os

    FILE_DIR = './DATA/'
    print(f'os.path.exists(FILE_DIR) => {os.path.exists(FILE_DIR)}')
    if not os.path.exists(FILE_DIR):
        os.makedirs(FILE_DIR)

    # 폴더 안에 파일 생성 및 데이터 기록
    file = open(FILE_DIR + 'data2.txt', mode='a', encoding='utf-8')
    file.write('하하하하\n')
    file.close()

if 1:
    try:
        # 데이터 저장 폴더에 파일 저장하기
        FILE_DIR = './DATA/'
        # 폴더 안에 파일 생성 및 데이터 기록
        file = open(FILE_DIR + 'data4.txt', mode='w', encoding='utf-8')
        file.write('ㅋㅋㅋㅋ\n')

    except FileNotFoundError:
        print(f"파일 또는 폴더가 존재하지 않습니다.")
    else:
        file.write("ㅎㅎㅎㅎ\n")
        file.close()






