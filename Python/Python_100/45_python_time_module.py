# Python Time 모듈 사용하기
# 현재 연도 출력해보기

import time

a = time.gmtime()

print(a)
# time.struct_time(tm_year=2021, tm_mon=3, tm_mday=5, tm_hour=6, tm_min=36, tm_sec=47, tm_wday=4, tm_yday=64, tm_isdst=0)

b = a.tm_year
print(b)