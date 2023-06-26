#Question: Simplify Path
##Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
# The canonical path should have the following format:
# The path starts with a single slash '/'.
# Any two directories are separated by a single slash '/'.
# The path does not end with a trailing '/'.
# The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
# Return the simplified canonical path.

#Approach:
# The code uses a stack to simplify a given absolute path in a Unix-style file system. It iterates over each component of the path, ignoring empty or '.' components. If a component is '..', it pops the top element from the stack to go up one level in the directory hierarchy. Otherwise, it pushes the directory onto the stack. Finally, it constructs the simplified canonical path by joining the elements in the stack with '/' as the separator.

# Time complexity: O(n)

# Space complexity: O(n)

def simplifyPath(path):
    stack=[]

    components=path.split('/')

    for c in components:
        if c=='' or c=='.':
            continue
        elif c=='..':
            if stack:
                stack.pop()
        else:
            stack.append(c)
    
    simplified_path="/"+"/".join(stack)

    return simplified_path


path = "/home/"
print(simplifyPath(path))
# Expected Output: "/home"