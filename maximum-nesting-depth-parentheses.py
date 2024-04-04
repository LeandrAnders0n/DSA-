#Question: 1614. Maximum Nesting Depth of the Parentheses
# A string is a valid parentheses string (denoted VPS) if it meets one of the following:
# It is an empty string "", or a single character not equal to "(" or ")",
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:
# depth("") = 0
# depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.
# Given a VPS represented as string s, return the nesting depth of s.

#Approach:
# Initialize `max_count` and `count` to zero, then iterate through each character in `s`. If an opening parenthesis is encountered, increment `count` and update`max_count` to the maximum of its current value and `count`. If a closing parenthesis is encountered, `count` is decremented. Finally, the method returns `max_count`, representing the deepest level of nested parentheses in the string.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxDepth(self, s: str) -> int:
        max_count, count = 0, 0
        for c in s:
            if c == "(":
                count+=1

                max_count = max(max_count, count)

            if c == ")":
                count-=1
            

        return max_count
sol=Solution()

# Example 1:
s = "(1+(2*3)+((8)/4))+1"
print(sol.maxDepth(s))
# Expected Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:
s = "(1)+((2))+(((3)))"
print(sol.maxDepth(s))
# Expected Output: 3
 
