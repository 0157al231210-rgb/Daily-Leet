class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        dif = float("inf")
        for i in range(len(nums)):
            if nums[i] == target:
                dif = min(dif,abs(i - start))
        return dif