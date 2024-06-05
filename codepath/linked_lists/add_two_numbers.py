from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode() # new node initialized
        current = new_node # current pointer pointing to the new node
        carry = 0

        while l1 or l2:
            sum = carry # later to be added to our sum

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10 
            sum = sum % 10
            current.next = ListNode(sum) # create node with value sum
            current = current.next # update current pointer

        # case where one of the list has no nodes left, so current's next is pointed to the remaining carry
        if carry == 1:
            current.next = ListNode(1)

        return new_node.next

# create linked lists from lists
def create_linked_lists(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    # head is gonna stay exactly where it is since we want to return the start position (head) of the newly created linked list
    return head

# print linked list
def print_linked_list(node: Optional[ListNode]) -> None:
    while node:
        print(node.val, end="->")
        node = node.next
    print("None")

def main():
    l1 = create_linked_lists([5,6,4])
    l2 = create_linked_lists([2,4,3])

    print("list 1:")
    print_linked_list(l1)

    print("list 2:")
    print_linked_list(l2)

    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    print("result after addition:")
    print_linked_list(result)
    

if __name__ == "__main__":
    main()