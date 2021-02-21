# 2-gram 문자열에서 2개의 연속된 요소를 출력하는 방법
# python -> 2-gram -> py, yt, th...
# 2-gram 출력 프로그램 만들기

def make_2_gram(words:str) -> str:
    for index in range(len(words)-1):
        print(words[index:index+2])

make_2_gram(input())


data = input()
for i in range(len(data)-1):
    print(data[i], data[i+1], sep='')

'''
py
yt
th
ho
on
'''