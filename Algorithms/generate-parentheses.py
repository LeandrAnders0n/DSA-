#Question:Generate Parentheses
# Given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of well-formed(balanced) parentheses.
#Approach:
# Generate all possible combinations of balanced parentheses using recursion. We define a function dfs that recursively constructs valid combinations by adding open or close parentheses based on certain conditions. 
# Time Complexity: O(2^n)
# Space Complexity:  O(n)

def all_parenthesis(n):
        #User function Template for python3
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 
    
            if left < n:
                dfs(left + 1, right, s + '(')
    
            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res
        



n = 1
# Output:
# ()
print(all_parenthesis(n))
n = 3
# Output:
# ((()))
# (()())
# (())()
# ()(())
# ()()()
print(all_parenthesis(n))
