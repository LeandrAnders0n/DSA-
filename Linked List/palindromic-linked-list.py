#Question: 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

#Approach: Two Pointer
# Utilize a two-pointer technique to find the midpoint of the linked list. Then, reverse the first half of the list in place. After that, compare each node of the reversed first half with the corresponding node of the second half. 

# Time Complexity: O(n)
# Space Complexity: O(1) 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True  

        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        if fast:
            slow = slow.next

        while slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
            
        return True


# Example 1:
head = [1,2,2,1]
# Expected Output: true

# Example 2:
head = [1,2]
# Expected Output: false