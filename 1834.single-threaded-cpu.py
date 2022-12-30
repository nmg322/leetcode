#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#

# @lc code=start
from typing import List

from functools import total_ordering
import heapq

@total_ordering
class MyCustomList(list):
    def _is_valid_operand(self, other):
        return (len(self)==3 and len(other)==3)

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self[1]==other[1] and self[2]==self[2])

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self[1]<other[1]) or  (self[1]==other[1] and self[2]<other[2]))

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        tasks = [MyCustomList(tasks[i] + [i]) for i in range(N)]
        tasks.sort(key=lambda x: x[0], reverse=True)
        available_tasks, processing_order = [], []
        curr_time= 1
        while len(processing_order)<N:
            while len(tasks)>0 and (tasks[-1][0] <= curr_time):
                heapq.heappush(available_tasks, tasks.pop())
            if len(available_tasks)==0:
                curr_time = tasks[-1][0]
                continue
            curr_task = heapq.heappop(available_tasks)
            processing_order.append(curr_task[2])
            curr_time += curr_task[1]
        return processing_order

# @lc code=end

