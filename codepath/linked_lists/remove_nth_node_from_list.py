"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if not head:
        #     return None

        # current = head
        # length = 1
        # while current:
        #     length += 1
        #     current = current.next

        # if n > length:
        #     return head

        # if n == length:
        #     return head.next

        # current = head
        # node_to_be_deleted = length - n
        # for _ in range(node_to_be_deleted - 1):
        #     current = current.next
        
        # if current.next:
        #     current.next = current.next.next
        
"""
"""
# correct solution
# return head
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        # move first to a position where its 'n-1' position away from second
        for _ in range(n+1):
            first = first.next

        # move second to its correct position
        while first:
            first = first.next
            second = second.next

        # second is just before the node we wanna delete
        second.next = second.next.next

        return dummy.next
"""