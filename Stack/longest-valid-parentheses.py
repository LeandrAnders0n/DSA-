# Question:Longest Valid Parentheses
# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring
#Approach:
#Create a Hash Map with the mapping of the opening and closing brackets. Loop through every character in the string, if the bracket, is an opening brakcket, add it to the stack
#Else check if there is a matching opening bracket for the closing one, and if so, pop it and increment the counter
#Continue until you reach the end of the string
# Time Complexity: O(n) 
# Space Complexity: O(n)

def valid_parentheses(s):

    brackets={
        "(":")",
        "{":"}",
        "[":"]",
    }

    count=0
    stack=[]

    for c in s:
        if c in "{([":
            stack.append(c)
        else:
            if stack:
                if brackets[stack[-1]]==c:
                    stack.pop()
                    count+=1
    return count
    
s = "(()"
print(s)
print(valid_parentheses(s))
s = "(())"
print(s)
print(valid_parentheses(s))

