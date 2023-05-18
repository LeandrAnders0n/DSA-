#Depth First Graph Traversal
# The graph starts from the source node, visiting each node and its neighbors in a depth-first manner.
# We use a stack to keep track of the nodes to be visited and prints the visited nodes.
#Time Complexity: O(n + m)
#The time complexity is linear with respect to the number of node (n) and edges (m) in 
#Space Complexity: O(n)

graph={
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':['F'],
    'E':[],
    'F':[],
}

def dfs(graph,source):
    stack=[]
    stack.append(source)
    while stack:
        current=stack.pop()
        print(current)
        for node in graph[current]:
            stack.append(node)

dfs(graph,'A')
