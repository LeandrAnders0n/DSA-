#Question:Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

#Approach:
# Iterate through both lists, comparing values, and merge them into a new sorted list. 

# Time Complexity: O(m + n), where m and n are the lengths of the input lists
# Space Complexity: is O(1) 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_list(list1,list2):
    cur = dummy = ListNode()
    while list1 and list2:               
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2
            
    if list1 or list2:
        cur.next = list1 if list1 else list2
        
    return dummy.next