# 키보드로 거북이를 조종해서 그림 그리기
import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

while True :
    if  t.onkeypress(turn_right) :
         t.onkeypress(turn_right, "Right")
         
    if t.onkeypress(turn_up) :
            t.onkeypress(turn_up, "Up")
            
    if t.onkeypress(turn_left) :
        t.onkeypress(turn_left, "Left")

    if t.onkeypress(turn_down) :
            t.onkeypress(turn_down, "Down")


# 화면 지우기
def blank():
    t.clear()

t.shape("turtle")                   # 거북이 모양 사용
t.speed(0)                          # 거북이 속도를 가장 빠르게

t.onkeypress(blank, "Escape")       # ESC 누르면 blank 함수 실행
t.listen()                          # 거북이 그래픽 창이 키보드 입력을 받습니다.
