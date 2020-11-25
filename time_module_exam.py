# -------------------------------------------
# time 모듈 사용
# -------------------------------------------
import time

# time 모듈 안에 어떤 함수나 변수가 있는지 어떻게 확인
dicts = time.__dict__
# for item in dicts.items() : print(item)

# time모듈 함수 사용
print(f"{time.time()}")


# 현재 시간 정보 반환
cur_time = time.ctime()
print(f"{type(cur_time)}, {cur_time}")

# 시간 쪼개기
cur_time = time.ctime().split()
print(cur_time)
hms = cur_time[-2].split(':')
print(f"지금은{hms[0]}시 {hms[1]}분 {hms[2]}초 입니다.")
print('')

# time에서 반환한 값을 날짜와 시간 형태로 변환
data_time = time.localtime(time.time())
print(type(data_time), {data_time})
print('')

print({data_time.tm_year}, {data_time.tm_mon})
print({data_time.tm_wday}, '(월~일 : 0 ~ 6)')
print(data_time.tm_yday)

# strftime('포맷', 시간객체) : 날짜 / 시간 포맷 설정
data_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(f"data_time => {data_time}")

data_time = time.strftime('%c', time.localtime(time.time()))
print(f"data_time => {data_time}")
