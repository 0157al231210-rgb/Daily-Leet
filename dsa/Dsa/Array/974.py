class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        res = 0
        prefixCnt = {0:1}
        
        for n in nums:
            prefixSum += n
            remain = prefixSum % k

            res += prefixCnt.get(remain,0)
            prefixCnt[remain] = 1 + prefixCnt.get(remain, 0)

        return res