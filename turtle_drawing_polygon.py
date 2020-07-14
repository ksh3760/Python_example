import turtle as t

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n, a):
    for x in range(n):
        t.forward(a)
        t.left(360/n)

polygon(3)  # 삼각형을 그립니다.
polygon(5)  # 오각형을 그립니다.

# 그림을 그리지 않고 거북이를 100만큼 이동합니다.

t.up()              # 꼬리를 올림
t.forward(100)      # 앞으로 100
t.down()            # 꼬리를 내림

polygon2(3, 75)     # 한 변이 75인 삼각형을 그립니다.
polygon2(5, 100)    # 한 변이 100인 오각형을 그립니다.
