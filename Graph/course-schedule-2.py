#Question: 210. Course Schedule II
# There are a total of n courses you have to take, labeled from 0 to n - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
 
#Approach: Topological Sort
# The code is initiated with the creation of data structures: an adjacency list, a result list, and lists to track in-degrees and visited nodes. The directed graph is constructed from given prerequisites, and in-degrees are updated accordingly. A topological sort is executed through a queue, appending courses to the result and adjusting in-degrees. Cycles are checked passively by ensuring that the count of visited nodes equals the total number of courses.

#Time and Space Complexity: O(V + E)

from collections import deque
from typing import List

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Initialization
        adj=[[0] for _ in range(n)]
        ans=[]
        visited=set()
        indegree=[0]*n
        
        # Step 2: Build Graph and In-degrees
        for p in prerequisites:
            course=p[0]
            pre=p[1]
            adj[pre].append(course)
            indegree[course]+=1

        # Step 3: Topological Sort using Queue
        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)

        while queue:
            current=queue.popleft()
            ans.append(current)
            visited.add(current)

            for next_course in adj[current]:
                indegree[next_course]-=1
                if indegree[next_course]==0:
                    queue.append(next_course)
        
        # Step 4: Check for Cycles
        if len(visited)!=n:
            return []
     
        # Step 5: Return the Result
        return ans

s=Solution()
# Example 1:
n = 2
prerequisites = [[1,0]]
print(s.findOrder(n,prerequisites))
# Expected Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:
n = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(s.findOrder(n,prerequisites))
# Expected Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# Example 3:
n = 1
prerequisites = []
print(s.findOrder(n,prerequisites))
# Expected Output: [0]