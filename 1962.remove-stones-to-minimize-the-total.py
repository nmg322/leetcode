#
# @lc app=leetcode id=1962 lang=python3
#
# [1962] Remove Stones to Minimize the Total
#

# @lc code=start
from typing import List

import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]

        heapq.heapify(piles)
        for i in range(k):
            curr_max = -heapq.heappop(piles)
            heapq.heappush(piles, -(curr_max - curr_max//2))

        return -sum(piles)

# @lc code=end

