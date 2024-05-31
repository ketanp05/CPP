class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head: Node) -> None:
    if not head or not head.next:
        return 

    def split_list(head: Node) -> tuple[Node, Node]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # second_half is the start of the second half of the list
        second_half = slow.next

        # split the list by pointing slow to none
        slow.next = None

        return head, second_half
