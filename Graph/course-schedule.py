#Question:207. Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

#Approach: Topological sort
# In the given code, a directed graph is constructed to represent courses and their prerequisites. The in-degrees of each course are calculated based on the prerequisites. Subsequently, a topological sort is performed using a queue, where courses with no prerequisites are dequeued and their neighbors' in-degrees are reduced. The resulting order of courses is stored in the variable 'ans'. The function returns True if the length of 'ans' equals the total number of courses (n), indicating that all courses can be completed in a valid order; otherwise, it returns False.

#Time and Space Complexity: O(V + E)

from typing import List
from collections import deque

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == n

s=Solution()
# Example 1:
numCourses = 2
prerequisites = [[1,0]]
print(s.canFinish(numCourses,prerequisites))
# Expected Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(s.canFinish(numCourses,prerequisites))
# Expected Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.