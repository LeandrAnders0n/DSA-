# Question: 621. Task Scheduler
# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
# ​Return the minimum number of intervals required to complete all tasks.
 
#Approach: Greedy Method
# Utilize a greedy approach to minimize the number of intervals required to complete all tasks with a given cooling time constraint. Calculate the maximum frequency of any task and determine how many intervals are needed based on this frequency and the cooling time. Ensure that tasks with the highest frequency are scheduled first, respecting the cooling time constraint. 

# Time complexity & Space complexity: O(n)

from collections import Counter
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)

        max_freq = max(task_counts.values())

        max_count = sum(1 for count in task_counts.values() if count == max_freq)

        intervals = (max_freq - 1) * (n + 1) + max_count

        return max(intervals, len(tasks))
s=Solution()
# Example 1:
tasks = ["A","A","A","B","B","B"]
n = 2
print(s.leastInterval(tasks,n))
# Expected Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

# Example 2:
tasks = ["A","C","A","B","D","B"]
n = 1
print(s.leastInterval(tasks,n))
# Expected Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:
tasks = ["A","A","A", "B","B","B"]
n = 3
print(s.leastInterval(tasks,n))
# Output: 10
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.