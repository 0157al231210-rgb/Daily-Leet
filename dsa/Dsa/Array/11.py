class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        result = 0
        while left<right:
            if height[left]<height[right]:
                temp = height[left] * (right - left)
                if result < temp:
                    result = temp
                else:
                    left+=1
            else:
                temp = height[right] * (right - left)
                if result < temp:
                    result = temp
                else:
                    right-=1
        return result