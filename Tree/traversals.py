class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order(root):
    #bfs
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
    
#type of dfs
def in_order(root):
    #left,root,right
    if root is None:
        return

    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)

def pre_order(root):
    #root,left,right
    if root is None:
        return

    print(root.data, end=" ")
    pre_order(root.left)
    pre_order(root.right)

def post_order(root):
    #left,right,root
    if root is None:
        return

    post_order(root.left)
    post_order(root.right)
    print(root.data, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal:")
level_order(root)
print()

print("In order traversal:")
in_order(root)
print()

print("Pre order traversal:")
pre_order(root)
print()

print("Post order traversal:")
post_order(root)
