#Question: Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

#Approach: Stack
# Use a stack to process the tokens, performing arithmetic operations on the last two elements when encountering operators. 

# Time & Space  Complexity: O(n)

def evalRPN(tokens):
    stack=[]
    for t in tokens:
        if t not in "-*/+":
            stack.append(int(t))
        else:
            b,a=stack.pop(),stack.pop()
            if t=="+":
                stack.append(a+b)
            elif t=="-":
                stack.append(a-b)
            elif t=="*":
                stack.append(a*b)
            else:
                stack.append(int(a/b))
    return stack[0]

tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))
# Output: 9
# Explanation: ((2 + 1) * 3) = 9


tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))
# Output: 6
# Explanation: (4 + (13 / 5)) = 6


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22