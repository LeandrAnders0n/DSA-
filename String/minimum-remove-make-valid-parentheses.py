#Question: 1249. Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 
#Approach:
# Traverse the input string while keeping track of the counts of left and right parentheses encountered. Utilize a stack to maintain the order of encountered parentheses characters. During the traversal, if a left parenthesis is encountered, `left_count` is incremented; if it's a right parenthesis, `right_count` is incremented. If the count of right parentheses exceeds that of left ones, indicating an imbalance,  correct this imbalance by decrementing `right_count`. Otherwise, the character is added to the stack. After processing the string,  construct the final result by popping characters from the stack. If there are more left parentheses than right ones, decrement `left_count` and add the character to the result. Otherwise, appends the character directly. Finally, return the reversed `result` string, ensuring the correct order of characters. 

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_count = 0
        right_count = 0
        stack = []

        for ch in s:
            if ch == '(':
                left_count += 1
            elif ch == ')':
                right_count += 1
            if right_count > left_count:
                right_count -= 1
            else:
                stack.append(ch)

        result = ""
        
        while stack:
            current_char = stack.pop()
            if left_count > right_count and current_char == '(':
                left_count -= 1
            else:
                result += current_char

        return result[::-1]
sol=Solution()
# Example 1:
s = "lee(t(c)o)de)"
print(sol.minRemoveToMakeValid(s))
# Expected Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:
s = "a)b(c)d"
print(sol.minRemoveToMakeValid(s))
# Expected Output: "ab(c)d"

# Example 3:
s = "))(("
print(sol.minRemoveToMakeValid(s))
# Expected Output: ""
# Explanation: An empty string is also valid.