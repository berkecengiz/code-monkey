"""
** Reverse a singly linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def stringify_list(self):
        curr = self
        string = ""
        while curr:
            string += str(curr.val) + " -> "
            curr = curr.next
        return string + "None"


# Solution 1: Iterative
# Time: O(n)
# Space: O(1)
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# Solution 2: Recursive
# Time: O(n)
# Space: O(n)
def reverse_list_recursive(head):
    if not head or not head.next:
        return head

    p = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return p


# Test Cases

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(reverse_list(head).stringify_list())
