# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class ReverseLinkedList:
#     def reverse_list(self, head: Optional[Node]) -> Optional[Node]:
#         pass

# ===============================================================================================================================

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         pass

# ===============================================================================================================================

# 1st approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
    
# 2nd approach
