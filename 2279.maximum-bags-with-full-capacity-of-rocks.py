#
# @lc app=leetcode id=2279 lang=python3
#
# [2279] Maximum Bags With Full Capacity of Rocks
#

# @lc code=start
from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        N = len(capacity)
        for i in range(N):
            capacity[i] -= rocks[i]
        capacity.sort()

        i = 0
        while (i < N) and (additionalRocks >= capacity[i]):
            additionalRocks -= capacity[i]
            i += 1

        return i
        
# @lc code=end

