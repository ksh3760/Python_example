# 1부터 n까지의 합을 구하는 함수를 생성합니다.
# this function calculates the sum from 1 to n
def sum_func(n):
    s = 0
    for x in range(1, n+1):
        s = s + x
    return s

print(sum_func(10))
print(sum_func(100))
