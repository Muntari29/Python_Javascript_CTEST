# 문자열 리스트 뒤집기
# 단 함수는 어떠한 리턴값도 없어야 한다. 리턴 없이 리스트 내부를 조작하라

s = ["h","e","l","l","o"]

class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

# reverse() VS reversed() 차이 알기

print(reversed(s))
# <list_reverseiterator object at 0x7f90e3a3f2b0>
print(list(reversed(s)))
# ['o', 'l', 'l', 'e', 'h']
print(s)
# ['h', 'e', 'l', 'l', 'o']

v =  ["h","e","l","l","o", "GO"]

print(v.reverse())
# None
print(v)
# ['GO', 'o', 'l', 'l', 'e', 'h']

s = s[::-1]
print(s)