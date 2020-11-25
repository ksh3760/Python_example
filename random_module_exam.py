# ----------------------------------------------
# random 모듈 사용 : 임의의 수 (난수) 관련 기능
# ----------------------------------------------
import random

# random() : 0.0 <= ~ < 1.0 사이 임의의 실수(float) 반환
print({random.random()})

# uniform(a, b) : a <= ~ <= b 사이 임의의 실수(float)반환
print(random.uniform(5, 10))

# randint(a, b) : a <= ~ <= b 사이 임의의 정수(int) 반환
print(random.randint(5, 10))

# randrange(stop)        : 0 <= ~ < stop 사이 정수(int) 반환
# randrange(std, stop)   : std <= ~ < stop 사이 정수(int) 반환
print(random.randrange(1, 7))
print(random.randrange(1, 7, 2))
print(random.randrange(10))

# shuffle(x) : 순서형 자료(sequence)를 뒤죽박죽으로 섞어놓는 함수
abc = ['a', 'b', 'c', 'd', 'e']
random.shuffle(abc)

# choice(x) : 순서형 자료(sequence)에서 하나 뽑기
print(random.choice(abc))
