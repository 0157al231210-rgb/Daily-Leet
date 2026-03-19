class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax,curMin = 1,1
        for i in nums:
            if i == 0:
                curMax,curMin = 1,1
                continue
            tmp = curMax * i
            curMax = max(tmp , curMin * i, i)
            curMin = min(tmp , curMin * i, i)
            res = max(res, curMax)
        return res