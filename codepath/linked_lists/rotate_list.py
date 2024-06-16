from typing import Optional, List

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def rotation(self, head:Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        current = head
        lenght = 1
        while current.next: #O(n)
            lenght += 1
            current = current.next

        # update k, to avoid rotaions
        k = k%lenght
        if k == 0:
            return head
        
        # make our list circular
        current.next = head

        # now my head is the tail in this moment
        current_tail = head

        # move current tail just before my new head
        moves = lenght-k
        for _ in range(moves-1):
            current_tail = current_tail.next

        new_head = current_tail.next
        
        # in this part we have finished rotation, point current_tail to none
        current_tail.next = None

        return new_head
        

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next

    return head

# print linked list
def print_linked_list(node: Optional[ListNode]):
    while node:
        print(node.val, end="->")
        node = node.next
    print("None")

def main():
    values = [1,2,3,4,5]
    k = 3 # number of rotations
    
    head = create_linked_list(values)
    print_linked_list(head) # before rotation

    s = Solution()
    head = s.rotation(head, k)

    print_linked_list(head) # after rotation

if __name__ == "__main__":
    main()