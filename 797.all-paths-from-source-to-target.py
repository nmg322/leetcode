#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)

        dp = [None for i in range(N)]; dp[N-1] = [[N-1]]

        def traverse(curr_node=0):
            if dp[curr_node] is None:
                paths = []
                for n in graph[curr_node]:
                    ret_paths = traverse(n)
                    for p in ret_paths:
                        p = [curr_node] + p
                        paths.append(p)
                dp[curr_node] = paths

            return dp[curr_node]

        return traverse()

# @lc code=end

