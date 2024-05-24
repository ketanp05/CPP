from typing import List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MergeTwoSortedLists:
    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode() # initializing the dummy node
        tail = dummy # initially tail is pointing to dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2 # for the remaining nodes of the list which are to be attached to the merged list.

        return dummy.next
    
    def create_linked_list(self, lst: List) -> ListNode:
        dummy = ListNode()
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
    
    def print_linked_list(self, head: ListNode) -> ListNode:
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

def main():
    try:
        mtsl = MergeTwoSortedLists()
        # list1, list2 = mtsl.create_linked_list([1,2,4]), mtsl.create_linked_list([1,3,4])
        # list1, list2 = mtsl.create_linked_list([]), mtsl.create_linked_list([])
        list1, list2 = mtsl.create_linked_list([]), mtsl.create_linked_list([0])
        merged_head = mtsl.merge_two_lists(list1, list2)
        mtsl.print_linked_list(merged_head)
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        print("Execution done/over/finished/khatam")


if __name__ == "__main__":
    main()