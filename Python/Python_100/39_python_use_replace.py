# 오타 수정하기
# 입력되는 모든 q 를 e로 바꾸는 프로그램 만들기
# ex) querty  / La viq qn rosq

user_input = input()

words = []

for text in user_input:
    if text == 'q':
        words.append('e')
    else:
        words.append(text)

print(*words, sep='')

n = input()
print(n.replace('q', 'e'))

# replace(old, new, [count]) -> 
## replace("찾을값", "바꿀값", [바꿀횟수])
