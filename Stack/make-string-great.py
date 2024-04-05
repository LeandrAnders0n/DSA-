#Question: 1544. Make The String Great
# Given a string s of lower and upper case English letters.
# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
# Notice that an empty string is also good.

#Approach:
# To solve the problem, a stack is utilized to simulate the removal of adjacent characters that create a "bad" string. The function iterates through each character in the input string, checking whether the current character combined with the top character of the stack forms a pair of characters that need removal due to being the same letter with different cases. If such a pair is identified, the top character is popped from the stack; otherwise, the current character is pushed onto the stack. After iterating through the entire string, the characters remaining in the stack are joined together to form the resulting "good" string, which is then returned.

# Time & Space Complexity: O(n)

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

sol=Solution()
# Example 1:
s = "leEeetcode"
print(sol.makeGood(s))
# Expected Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

# Example 2:
s = "abBAcC"
print(sol.makeGood(s))
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""

# Example 3:
s = "s"
print(sol.makeGood(s))
# Expected Output: "s"