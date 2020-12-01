# # 1 ~ 100 사이의 3의 배수 합
# # 10개만
# from EXAM_EXCEPT.moduleA import ThreeMultipleCheck
# from EXAM_EXCEPT.moduleA import NotThreeMultipleError
#
# x = 0
#
# for i in range(1, 101):
#     try:
#         x += ThreeMultipleCheck(i)
#     except NotThreeMultipleError(Exception):
#         print('3의 배수가 아닙니다.')
#


# 다른 파일에 존재하는 클래스, 함수 가져오기
# from EXAM_EXCEPT.moduleA import ThreeMultipleCheck
from pythonProject.EXAM_EXCEPT.moduleA import *

# 3의 배수(1 ~ 100사이) 10개 합을 출력하기
threeSum = 0

for cnt in range(10):
    try:
        threeSum += three_multiple()
        print(f"threeSum = {threeSum}")

    except NotThreeMultipleError as ne:
        pass

print(f"1부터 100까지 3의 배수 10개 합 : {threeSum}")