import turtle as t

t.bgcolor("black")          # 배경색을 흑색으로 지정
t.speed(0)                  # 속도를 가장빠르게 지정

for x in range(200):        # 0 부터 199 까지
    if x % 3 == 0:          # 번갈아 가면서 선 색을 바꿈
        t.color("red")
    if x % 3 == 1:
        t.color("yellow")
    if x % 3 == 2:
        t.color("blue")

    t.forward(x * 2)        # x*2 만큼 앞으로 이동합니다(반복하면서 선이 점점 길어짐)
    t.left(119)             # 거북이를 119도 왼쪽으로 회전
