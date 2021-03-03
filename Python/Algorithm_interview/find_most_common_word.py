# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자를 구분하지 않으며, 마침표, 쉼표등의 구두점은 무시한다.
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# case 1, 2 모두 충족해야함

import re
import collections
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# paragraph_2 = "a, a, a, a, b,b,b,c, c"

banned = ["hit"]
# banned_2 = ["a"]

class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        lower_paragraph = [char for char in re.sub(r'[^\w]', ' ',paragraph).lower().split()]
        dict_paragraph = {}

        for key in lower_paragraph:
            if key not in banned:
                count = lower_paragraph.count(key)
                dict_paragraph[key] = count

        word = [key for key, value in dict_paragraph.items() if max(dict_paragraph.values()) == value]
        
        return word[0]


# 조금 더 효율이 좋은 답안

class Solution_better_answer:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        lower_paragraph = [char for char in re.sub(r'[^\w]', ' ',paragraph).lower().split() if char not in banned]
        counts = collections.Counter(lower_paragraph)
        return counts.most_common(1)[0][0]


