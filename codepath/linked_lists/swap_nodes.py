from typing import Optional, List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swap_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current and current.next: # O(n)
            first = current
            second = current.next

            # move prev and swap
            first.next = second.next
            second.next = first
            prev.next = second

            # move pointers
            prev = first
            current = first.next

        return dummy.next

def create_linked_lists(nums: List[int]) -> Optional[ListNode]:
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for values in nums[1:]:
        current.next = ListNode(values)
        current = current.next
    return head


def print_linked_lists(node: Optional[ListNode]) -> None:
    while node:
        print(node.val, end="->")
        node = node.next
    print("None")

def main():
    s = Solution()

    nums = [1,2,3,4]
    head = create_linked_lists(nums)

    # before swapping
    print_linked_lists(head)

    # swapping
    result = s.swap_node(head)

    # after swapping
    print_linked_lists(result)

if __name__ == "__main__":
    main()