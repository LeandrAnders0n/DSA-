#Question:133. Clone Graph
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

#Approach:
#Use a depth-first search (DFS) approach to clone a graph, maintaining a `visited` dictionary to store cloned nodes. Recursively traverse the original graph, creating or retrieving cloned nodes and connecting them. The process starts from the given input node, and the cloned graph is returned. If the input node is `None`, the function returns `None`.

#Time & Space Complexity: O(n)

# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            
            if(node in visited):
                return visited[node]
            
            visited[node] = Node(node.val)
            
            for nei in node.neighbors:
                visited[node].neighbors.append(dfs(nei))
                
            return visited[node]
        
        if not node: return None
        
        visited = {}
        clone_graph = dfs(node)
        return clone_graph