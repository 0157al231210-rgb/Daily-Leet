class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = set([0])
        
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        for i in nums:
            subSum = set(Sum)
            for s in Sum:
                subSum.add(s + i)
            Sum = subSum
        
        return target in Sum