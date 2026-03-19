#Greedy technique
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSub = nums[0]
#         curSum = 0
#         for i in nums:
#             if curSum < 0:
#                 curSum = 0
#             curSum += i
#             maxSub = max(maxSub, curSum)
#         return maxSub


# 1D DP (Kadanes)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for i in nums:
            curSum = max(i, curSum + i)
            maxSub = max(maxSub, curSum)
        return maxSub
        