#Question:399. Evaluate Division
# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

#Approach:
# The graph is constructed using the provided equations and values, with bidirectional relations established for each division. Breadth-First Search is employed to traverse the graph, accumulating division values until the target node is reached. If a queried node is absent or unreachable, a result of -1.0 is assigned. The overall solution structure is organized and facilitates efficient evaluation of division equations.

# Time complexity is O(N + Q), where N is the number of equations, and Q is the number of queries
# Space complexity is O(N), where N is the number of equations

from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = self.buildGraph(equations, values)
        results = []
        
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                results.append(-1.0)
            else:
                result = self.bfs(dividend, divisor, graph)
                results.append(result)
        
        return results
    
    def buildGraph(self, equations, values):
        graph = defaultdict(dict)
        
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value
        
        return graph
    
    def bfs(self, start, end, graph):
        queue = deque([(start, 1.0)])
        visited = set()
        
        while queue:
            node, value = queue.popleft()
            
            if node == end:
                return value
            
            visited.add(node)
            
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    queue.append((neighbor, value * weight))
        
        return -1.0
    
s=Solution()
# Example 1:
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(s.calcEquation(equations,values,queries))

# Expected Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0

# Example 2:
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Expected Output: [3.75000,0.40000,5.00000,0.20000]
print(s.calcEquation(equations,values,queries))

# Example 3:
equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Expected Output: [0.50000,2.00000,-1.00000,-1.00000]
print(s.calcEquation(equations,values,queries))
