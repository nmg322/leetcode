#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value_state_table = [[None, None] for i in range(len(prices)+1)]; value_state_table[-1] = [0, 0]
        def _maxProfit(prices: List[int], idx: int = 0, state: int = 0) -> int:
            if idx>len(prices): return 0
            if value_state_table[idx][state] is None:
                if state==0:
                    value_state_table[idx][state] = max(_maxProfit(prices, idx+1, 1) - prices[idx], _maxProfit(prices, idx+1, 0))
                else: # current_state == '1'
                    value_state_table[idx][state] = max(_maxProfit(prices, idx+2, 0) + prices[idx], _maxProfit(prices, idx+1, 1))
            return value_state_table[idx][state]
        return _maxProfit(prices)      
# @lc code=end

