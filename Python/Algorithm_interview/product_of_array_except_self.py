# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라

'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''

nums = [1,2,3,4]
result = []
p = 1

for i in range(0, len(nums)):
    result.append(p)
    p = p * nums[i]

print(result)
print(p)

box = result

p = 1
for i in range(len(nums)-1, -1, -1):
    box[i] = result[i] * p
    p = p * nums[i]

print(result)
print(p)


# class Solution:q
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

        