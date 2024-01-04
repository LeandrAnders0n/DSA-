#Question: 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the number is negative
        if x < 0:
            return False
        
        copy_num = x
        new_num = 0

        while x:
            num = x % 10
            new_num = new_num * 10 + num
            x = x // 10

        return copy_num == new_num

s=Solution()
# Example 1:
x = 121
print(s.isPalindrome(x))
# Expected Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
x = -121
print(s.isPalindrome(x))
# Expected Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
x = 10
print(s.isPalindrome(x))
# Expected Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.