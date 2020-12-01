# 3의 배수 체크 함수
def three_multiple():
    pass
    # if  % 3 != 0:
    #     raise NotThreeMultipleError


# 3의 배수 Exception Class
class NotThreeMultipleError(Exception):  # Exception 상속
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')


if __name__ == "__main__":
    # 해당 파일이 실행 모드일 경우 동작 코드
    # 함수 호출하기 -----------------------------------
    try:
        pass
    except:
        pass