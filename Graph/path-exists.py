#Question:1971. Find if Path Exists in Graph
# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

#Approach:
# Use breadth-first search (BFS) using a queue, initialized with the start node. The graph is constructed using a defaultdict with sets to store neighbors of each node. The BFS explores nodes level by level, updating the queue with unvisited neighbors, and returns True if the end node is reached, indicating the existence of a valid path; otherwise, it returns False.

#Time and Space Complexity:O(V + E)

from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: list[list[int]], start: int, end: int) -> bool:
        queue=[start]
        visited=set()
        d=defaultdict(set)

        for i,j in edges:
            d[i].add(j)
            d[j].add(i)
        
        while queue:
            node=queue.pop(0)
            if node==end:
                return True
            
            for n in d[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        
        return False

s=Solution()
#Example 1
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(s.validPath(n,edges,source,destination))
#Expected Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2

#Example 2
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
print(s.validPath(n,edges,source,destination))
# Expected Output: false
# Explanation: There is no path from vertex 0 to vertex 5.