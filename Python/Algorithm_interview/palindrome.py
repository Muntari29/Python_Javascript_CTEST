# 회문 판별하기
# 대소문자는 구분하지 않으며 영어와 숫자만을 대상으로 한다.
'''
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''
import re

# My answer

s = "A man, a plan, a canal: Panama"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s.lower():
            if char.isalnum():
                strs.append(char)
        return strs == strs[::-1]


# 정규식 이용 답안

class Solution_2:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        #정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '',s)
        return s == s[::-1]