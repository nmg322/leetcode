#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        max_idx = -1
        for curr_idx in range(N):
            max_idx = max(max_idx, nums[curr_idx]+curr_idx)
            if max_idx >= N-1:
                return True
            elif nums[curr_idx]==0 and max_idx<=curr_idx:
                return False
        return True

# @lc code=end

