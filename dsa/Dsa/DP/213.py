class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def case(arr):
            rob1,rob2 = 0,0
            for n in arr:
                tmp = max(rob1 + n, rob2)
                rob1 = rob2 
                rob2 = tmp
            return rob2
        
        if len(nums) == 1:
            return nums[0]
        
        return max(case(nums[:-1]), case(nums[1:]))