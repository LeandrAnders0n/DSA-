#Question: 442. Find All Duplicates in an Array
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

#Approach:
# Utilize the range constraint of the integers (from 1 to n) to map each integer to its corresponding index in the array. During traversal, each encountered number is then used to determine its appropriate index (by subtracting 1 due to zero-based indexing). If the number at this index is already negative, it implies that the current number has been encountered before, hence it's a duplicate, and it's added to the result list. Otherwise, the number at that index is negated to indicate its presence. 

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] *= -1

        return result

s=Solution()


# Example 1:
nums = [4,3,2,7,8,2,3,1]
print(s.findDuplicates(nums))
# Expected Output: [2,3]

# Example 2:
nums = [1,1,2]
print(s.findDuplicates(nums))
# Expected Output: [1]

Example 3:
nums = [1]
print(s.findDuplicates(nums))
# Expected Output: []
