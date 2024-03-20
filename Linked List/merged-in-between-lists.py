#Question: 1669. Merge In Between Linked Lists
# You are given two linked lists: list1 and list2 of sizes n and m respectively.
# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

# Approach:
# Merge the nodes of list2 into list1 between indices a and b (inclusive). Traverse list1 until the node before index a, then traverse list1 again to find the node after index b. Connect the end of list2 to the node after index b and return the modified list1. 

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr = list1
        for _ in range(a - 1):
            ptr = ptr.next
        
        qtr = ptr.next
        for _ in range(b - a + 1):
            qtr = qtr.next
        
        ptr.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = qtr
        
        return list1
s=Solution()
# Example 1:
list1 = [10,1,13,6,9,5]
a = 3
b = 4
list2 = [1000000,1000001,1000002]
print(s.mergeInBetween(list1,a,b,list2))
# Expected Output: [10,1,13,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

# Example 2:
list1 = [0,1,2,3,4,5,6]
a = 2
b = 5
list2 = [1000000,1000001,1000002,1000003,1000004]
print(s.mergeInBetween(list1,a,b,list2))
# Expected Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the result.