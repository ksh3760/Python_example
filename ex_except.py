# 예외처리 실습
# -----------------------------------------
if 0:
    var_a = list(map(int, input("정수를 입력하세요: ").split()))
    print(int(var_a[0] / var_a[1]))

# 0으로 나눗셈 진행 시 오류 발생 ---------------
if 0:
    while True:
        try:  # 예외 발생 가능 코드
            # 1) 2개 숫자 입력 받기
            nums = list(map(int, input("Enter 2 number : ").split()))

            # 2) 나눗셈하기
            # print(f"{nums[0]} / {nums[1]} = {nums[0] / nums[1]}")
            value = nums[0] / nums[1]

        except ZeroDivisionError:  # 예외 발생 처리 코드
            print("0으로 나눌 수 없습니다.")
            break

        except IndexError:  # 예외 발생 처리 코드
            print("리스트 인덱스 오류 => len(nums) : ", len(nums))
            break

        except Exception as e:  # 예외 발생 처리 코드
            print("ERROR 발생", e)
            break

        else:  # 예외 발생하지 않았을 경우
            print(f"{nums[0]} / {nums[1]} = {value}")

        finally:  # 무조건 실행
            print("--- Always ---")

    print("=====THE END=====")

# 강제 오류 발생 --------------------------------------------------------
if 0:
    try:
        x = int(input("3의 배수를 입력하세요 : "))

        if x % 3 != 0:  # 3의 배수가 아니면
            raise Exception('3의 배수가 아닙니다.')  # 예외를 발생시킨다.
        print(x)

    except Exception as e:  # 예외 발생 시
        print("예외가 발생하였습니다.", e)


# 5개의 정수를 입력받고 예외 시 예외발생 출력 --------------------------------
def myFunc():
    xList = list(input("5개의 정수를 입력하세요 : ").split())

    if len(xList) != 5:
        raise Exception("갯수가 5개가 아닙니다.")
    else:
        for data in x:
            if data.isdigit() == False:
                raise Exception('모두 정수가 아닙니다.')

    return xList


if 0:
    try:
        numList = list(map(int, myFunc()))
        print(f"Number Data => {numList}")

    except Exception as e:
        print("예외가 발생하였습니다.", e)


# ------------------------------------------------------------------------
# 사용자 정의 예외 만들기
# ------------------------------------------------------------------------

# 3의배수 체크 사용자정의 예외 ------------------------------------------------
class NotThreeMultipleError(Exception):  # Exception 상속
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')


def three_multiple():
    x = int(input('3의 배수를 입력하세요 : '))
    if x % 3 != 0:
        raise NotThreeMultipleError

    return x


# 함수 호출하기 -------------------------------------------------------------
try:
    value = three_multiple()
    print(f"value is {value}")
except NotThreeMultipleError as ne:
    print("Error", ne)
