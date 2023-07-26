"""
** Add Two Numbers **
Difficulty: Medium
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    dummy_head = ListNode(0)
    p, q, current = l1, l2, dummy_head
    carry = 0
    # Iterate through both lists
    while p is not None or q is not None:
        # Set x and y to the current value of the nodes
        x = p.val if p is not None else 0
        y = q.val if q is not None else 0
        # Calculate the sum and carry
        sum = carry + x + y
        carry = sum // 10
        # Create a new node with the sum
        current.next = ListNode(sum % 10)
        current = current.next
        # Move to the next node
        if p is not None:
            p = p.next
        if q is not None:
            q = q.next
    # Check if there's a carry left
    if carry > 0:
        current.next = ListNode(carry)
    # Return the head of the list
    return dummy_head.next


# Test the function
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
# 342 + 465 = 807
sum = add_two_numbers(l1, l2)
while sum is not None:
    print(sum.val)
    sum = sum.next
