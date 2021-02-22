# 단어의 갯수를 출력하는 프로그램 만들기
# ex) 저 넓은 세상을 네 눈앞에 그려봐 네 진심을 느껴봐
str_data = input().split()

word_list = list(str_data)

print(len(word_list))
# 9

print(word_list)
#['저', '넓은', '세상을', '네', '눈앞에', '그려봐', '네', '진심을', '느껴봐']

n = input()
l = list(n.strip().split())
print(len(l))