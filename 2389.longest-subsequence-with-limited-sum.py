#
# @lc app=leetcode id=2389 lang=python3
#
# [2389] Longest Subsequence With Limited Sum
#

# @lc code=start
from typing import List
import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        answer = []
        for q in queries:
            answer.append(bisect.bisect_right(prefix_sum, q))
        return answer
# @lc code=end

