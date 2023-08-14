#Question:m Coloring Problem
#Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that no two adjacent vertices of the graph are colored with the same color
#Approach: Backtracking
# Use backtracking to determine if the undirected graph with V vertices can be colored using at most k colors such that no adjacent vertices have the same color. Iterate through vertices and colors, checking if a color can be assigned without violating constraints. Return True if a valid coloring is possible, False otherwise.

# Time Complexity: The worst-case time complexity is exponential, approximately O(k^V), as each vertex can have k possible colors, and we explore all possible combinations.
# Space Complexity:O(V)

def graph_coloring(graph, k, V):
    colors=[0]*V
    
    def coloring(colors,i):
        if i==V:
            return True
        for c in range(1,k+1):
            flag=True
            
            for j in range(V):
                if graph[i][j]==1 and colors[j]==c:
                    flag=False
            if flag==True:
                colors[i]=c
                if coloring(colors,i+1)==True:
                    return True
                colors[i]=0
    
    if coloring(colors,0)==None:
        return False
    return True

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
k = 3  
V = 4  

result = graph_coloring(graph, k, V)
print(result)
