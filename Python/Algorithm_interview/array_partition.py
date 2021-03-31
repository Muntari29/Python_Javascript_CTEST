# n개의 페어를 이용한 min(a,b)합으로 만들 수 있는 가장 큰 수를 출력하라.
# result min(1, 2) + min(3, 4) => 4

from typing import List

nums = [1, 4, 3, 2]

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        pair = []
        nums.sort()
        
        for i in nums:
            pair.append(i)
            if len(pair) == 2:
                result += pair[0]
                pair.clear()
                
        return result


class Solution2:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = nums[::2]
        # result = [1, 3] ex nums = [1, 4, 3, 2]
        return sum(result)

