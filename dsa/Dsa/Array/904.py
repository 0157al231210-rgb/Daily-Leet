class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        count = 0
        freqMap = {}
        for r in range(len(fruits)):
            freqMap[fruits[r]] = 1 + freqMap.get(fruits[r],0)

            while len(freqMap) > 2:
                freqMap[fruits[l]] -= 1
                if freqMap[fruits[l]] == 0:
                    del freqMap[fruits[l]]
                l += 1

            res = max(res, r - l + 1)
        return res        
