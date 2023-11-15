#Question:1791. Find Center of Star Graph
# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

#Approach:
# Use set operations to find the center node of a tree represented by a list of edges. By converting the first two edges into sets, duplicate nodes are eliminated. The set intersection operation (&) then identifies the common nodes between the two sets, revealing the potential centers of the tree.

#Time and Space Complexity: O(n)

from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0])& set(edges[1])).pop()
    
# Example 1:
edges = [[1,2],[2,3],[4,2]]
s=Solution()
print(s.findCenter(edges))
# Expected Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

# Example 2:
edges = [[1,2],[5,1],[1,3],[1,4]]
print(s.findCenter(edges))
# Expected Output: 1