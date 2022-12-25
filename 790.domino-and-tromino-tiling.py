#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        M = int(1e9 + 7)
        T = [1, 2, 5]
        if n<4: return T[n-1]
        for i in range(4, n+1):
            ret = ((2*T[-1])%M + T[-3])%M
            T = T[1:] + [ret]
        return T[-1]
# @lc code=end

