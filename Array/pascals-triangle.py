#Question:118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it

#Approach:
# The code generates Pascal's Triangle up to a given number of rows (`numRows`). It employs nested loops to calculate each row by summing adjacent elements from the previous row, storing the result in the `result` list. If `numRows` is zero, an empty list is returned.

# Time and Space Complexity:O(numRows^2)

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      result=[]

      if not numRows:
        return result
      
      first_row=[1]
      result.append(first_row)

      for i in range(1,numRows):
        prev_row=result[i-1]
        current_row=[1]

        for j in range(1,i):
          current_row.append(prev_row[j-1]+prev_row[j])
        
        current_row.append(1)
        result.append(current_row)

      return result

s=Solution()
# Example 1:
numRows = 5
print(s.generate(numRows))
# Expected Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
numRows = 1
print(s.generate(numRows))
# Expected Output: [[1]]