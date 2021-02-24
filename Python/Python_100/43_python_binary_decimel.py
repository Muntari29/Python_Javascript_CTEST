# 2020년 요일 출력 프로그램 만들기
# 2020년 1월 1일은 수요일이다.
# 입력받는 두 값을 이용해 a월 b일이 몇 요일인지 반환하는 함수를 만드시오

import datetime
month = int(input())
day = int(input())

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

def findday(month, day):
    print(days[datetime.datetime(2021, month, day).weekday()])

findday(month, day)


import datetime
m = int(input())
d = int(input())
def findDay(a,b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day[datetime.date(2020,a,b).weekday()]
print(findDay(m,d))