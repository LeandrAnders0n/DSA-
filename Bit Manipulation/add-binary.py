#Question:67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum=bin(int(a,2)+int(b,2))
        return sum[2:]

 

s=Solution()
# Example 1:
a = "11"
b = "1"
print(s.addBinary(a,b))
# Expected Output: "100"

# Example 2:
a = "1010"
b = "1011"
print(s.addBinary(a,b))
# Expected Output: "10101"