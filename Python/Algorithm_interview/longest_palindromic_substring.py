# 가장 긴 팰린드롬(회문) 부분 문자열 구하기

# ex) "babad", "cbbd", '123454321
# answer : 'bab' or 'aba'

'''
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
'''

s = "123454321"

# cbbd 에서 걸림
class Solution:
    def longestPalindrome(self, s: str) -> str:
        strs = ""
        result = {}

        for char in s:
            strs += char
            if strs == strs[::-1]:
                result[len(strs)] = strs
            else:
                continue
        return result[max(result.keys())]
        

# Best answer
class Solution_2:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        #exception first
        if len_s <= 1: return s
        minStart, maxLen, i = 0, 1, 0
        while i < len_s:

            # 1_string validation
            if len_s - i <= maxLen / 2:
                break
            j, k = i, i

            # 2_pointer_expand validation
            while k < len_s - 1 and s[k] == s[k + 1]: 
                k += 1
            i = k + 1

            # 3_pointer_expand validation
            while k < len_s - 1 and j and s[k + 1] == s[j - 1]:
                k, j = k + 1, j - 1
            if k - j + 1 > maxLen:
                minStart, maxLen = j, k - j + 1
                print(minStart, maxLen+minStart)
        return s[minStart: minStart + maxLen]
    
a = Solution_2()
c = a.longestPalindrome(s)

print(c)