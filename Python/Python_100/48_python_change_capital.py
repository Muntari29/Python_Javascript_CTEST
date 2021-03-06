# 대소문자 바꿔서 출력하기
# ex) AAABBBcccddd
# aaabbbCCCDDD

strs = 'AAABBBcccddd'

result = ''

for char in strs:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()

print(result)
# aaabbbCCCDDD