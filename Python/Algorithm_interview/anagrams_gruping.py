# Anagram은 일반적으로 모든 원본 문자를 정확히 한 번 사용하여
# 다른 단어 나 구의 문자를 재배열하여 형성 된 단어 또는 문구이다.
# 애나그램을 그루핑해보자!!
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from typing import  List
strs = ["eat","tea","tan","ate","nat","bat"]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        
        for char in strs:
            key = ''.join(sorted(char))
            if key not in my_dict:
                my_dict[key] = [char]
            else:
                my_dict[key] += [char]
        
        return my_dict.values()

# [["eat","tea","ate"],["tan","nat"],["bat"]]

# my_dict
# {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}