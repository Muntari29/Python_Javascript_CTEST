'''
다음 리스트의 내장함수의 시간 복잡도가 O(1)이 아닌것은?

1)  l[i]   => O(1)
2)  l.append(5) => O(1)
3)  l[a:b] => O(n)
4)  l.pop() => O(1)
5)  l.clear() => O(1)
'''

# l[a:b] => n이라는 길이의 리스트 l일 경우 a, b의 인덱스를 알기 위해서는
# 객체 n개에 대한 조회가 필요하므로 O(n)이 된다.

