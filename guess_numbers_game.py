# 숫자추측하는 게임 입니다.
import random

n = random.randint(1, 30)

while True:
    x = input("추측하는 숫자를 입력하세요. : ")
    g = int(x)
    if g == n:
        print("정답입니다.")
        break
    if g < n:
        print("입력한 숫자보다 작습니다.")
    if g > n:
        prunt("입력한 숫자보다 큽니다.")
