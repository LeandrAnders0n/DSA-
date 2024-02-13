#Question: 2108. Find First Palindromic String in the Array
# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for a in words:
            if a==a[::-1]:
                return a
        return ""

s=Solution()
# Example 1:
words = ["abc","car","ada","racecar","cool"]
print(s.firstPalindrome(words))
# Expected Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.

# Example 2:
words = ["notapalindrome","racecar"]
print(s.firstPalindrome(words))
# Expected Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".

# Example 3:
words = ["def","ghi"]
print(s.firstPalindrome(words))
# Expected Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.

