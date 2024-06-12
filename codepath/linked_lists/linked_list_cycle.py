from typing import Optional

class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

class Solution:
    def has_cycles(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        # pointer initialization
        slow = head # start of the linked list
        fast = head.next # next node of the linked list

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
    
def create_cycle_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_node = None
    if pos == 0:
        cycle_node = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current
    if cycle_node:
        current.next = cycle_node
    return head

def main():
    # Creating a linked list with a cycle
    values = [3, 2, 0, -4]
    pos = 1
    head = create_cycle_list(values, pos)
    
    sol = Solution()
    print(sol.has_cycles(head))  # Output: True

if __name__ == "__main__":
    main()