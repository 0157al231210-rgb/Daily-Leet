class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        prev = '0'
        for i in target:
            if i != prev:
                count += 1
            prev = i
        return count