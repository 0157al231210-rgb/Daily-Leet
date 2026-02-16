class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevmap = {}
        for i, n in enumerate(nums):
            diff=target-1
            if diff in prevmap:
                return [prevmap(diff),i]
            prevmap[n]=i
        