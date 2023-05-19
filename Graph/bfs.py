#Breadth First Graph Traversal
# The graph starts from the source node, visiting each node and its neighbors in a breadth-first manner.
# We use a queue to keep track of the nodes to be visited and prints the visited nodes.
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

def bfs(graph,source):
    q=[]
    q.append(source)
    while q:
        current=q.pop(0)
        print(current)
        for node in graph[current]:
            q.append(node)

bfs(graph,'A')