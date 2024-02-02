#Question:1291. Sequential Digits
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

#Approach:
# Iterate through substrings of the string "123456789" using nested loops, converting each substring to an integer. If the resulting integer falls within the specified range, it is appended to the list `a`. The final list is then sorted before being returned. 
 
class Solution:
    def sequentialDigits(self, low, high):
        c = "123456789"
        a = []

        for i in range(len(c)):
            for j in range(i + 1, len(c) + 1):
                curr = int(c[i:j])
                if low <= curr <= high:
                    a.append(curr)

        a.sort()
        return a

s=Solution()

# Example 1:
low = 100
high = 300
print(s.sequentialDigits(low,high))
# Expected Output: [123,234]

# Example 2:
low = 1000
high = 13000
print(s.sequentialDigits(low,high))
# Expected Output: [1234,2345,3456,4567,5678,6789,12345]
 
