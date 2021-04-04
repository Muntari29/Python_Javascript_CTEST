# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라

'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''
from typing import List

nums = [1,2,3,4]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        # 위 이미지에서의 1번 왼쪽 곱샘 결과
        p = 1

        for i in range(0, len(nums)):
            result.append(p)
            p = p * nums[i]

        # 위 이미지에서의 2번 오른쪽 곱샘 결과 + result 변수 재활용!
        p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i] * p
            p = p * nums[i]

        return result