class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)
        for n in range(len(temps)):
            while stack and temps[n] > temps[stack[-1]]:
                index = stack.pop()
                res[index] = n - index
            stack.append(n)
        return res