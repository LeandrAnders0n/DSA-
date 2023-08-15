#Question: Burning Tree
# Given a binary tree and a node data called target. Find the minimum time required to burn the complete binary tree if the target is set on fire. It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.
# Note: The tree contains unique values.
#Approach:
# Perform a level-order traversal to find the target node and store parent nodes. Use BFS (Breadth-First Search) to calculate the minimum time by simulating the burning process from the target node to other nodes.
# Time & Space Complexity: O(N), where N is the total number of nodes in the binary tree

def min_time(root,target):
    q=[root]
    parent={}

    Tar=None

    while q:
        temp=q.pop(0)
        if temp.data==target:
            Tar=temp
        if temp.left:
            q.append(temp.left)
            parent[temp.left]=temp
        if temp.right:
            q.append(temp.right)
            parent[temp.right]=temp
        
        visited=set()
        queue=[Tar]
        time=0

        while queue:
            size=len(queue)

            for _ in queue:
                node=queue.pop(0)
                visited.append(node)

                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                if parent.get(node) and parent[node] not in visited:
                    queue.append(parent[node])
            if queue:
                time+=1
        return time