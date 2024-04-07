#Question:678. Valid Parenthesis String
# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

#Approach:
# In this code snippet, we're implementing a method called checkValidString, which continuously checks the validity of a given string s as we iterate through it. We maintain two lists, left_parentheses and asterisks, to store the indices of left parentheses '(' and asterisks '*', respectively. As we go through each character in the string, if we encounter a left parenthesis, we add its index to left_parentheses; if it's an asterisk, we add its index to asterisks; and if it's a right parenthesis ')', we try to pair it with a left parenthesis from left_parentheses. If there's no left parenthesis available, we try to pair it with an asterisk from asterisks. If there's neither, the string is deemed invalid, and we return False. After iterating through the string, we then check if there are any remaining unmatched left parentheses. We continue this process until we exhaust both left_parentheses and asterisks. Finally, we return True if there are no remaining unmatched left parentheses, indicating a valid string, or False otherwise.

# Time & Space complexity: O(n)

class Solution:
    def checkValidString(self, s: str) -> bool:
        left_parentheses = []
        asterisks = []
    
        for i, char in enumerate(s):
            if char == '(':
                left_parentheses.append(i)
            elif char == '*':
                asterisks.append(i)
            elif char == ')':
                if left_parentheses:
                    left_parentheses.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
    
        while left_parentheses and asterisks:
            if left_parentheses[-1] < asterisks[-1]:
                left_parentheses.pop()
                asterisks.pop()
            else:
                break
    
        return len(left_parentheses) == 0
sol=Solution()

# Example 1:
s = "()"
print(sol.checkValidString(s))
# Expected Output: true

# Example 2:
s = "(*)"
print(sol.checkValidString(s))
# Expected Output: true

# Example 3:
s = "(*))"
print(sol.checkValidString(s))
# Expected Output: true
 