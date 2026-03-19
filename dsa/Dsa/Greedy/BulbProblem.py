"""Given N bulbs, either on (1) or off (0).
Turning on ith bulb causes all remaining bulbs on
the right to flip.

Find the min number of switches to turn all the
bulbs on.

· Constraints:
. 1 ≤ N ≤ 1e5
· A[i] = {0, 1}"""


class Solution:
    def minFlips(self, A: List[int]) -> int:
        res = 0
        flip = 0
        for b in A:
            if b ^ flip == 0:
                res += 1
                flip ^= 1
        return res