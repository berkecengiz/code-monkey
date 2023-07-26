"""Implementation of a linked list in Python. """


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            if self.head is None or self.head.next is None:
                self.tail = self.head
            return

        cur = self.head
        while cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
                if cur.next is None:
                    self.tail = cur
                return
            cur = cur.next

    def insert(self, index, data):
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        cur = self.head
        for _ in range(index - 1):
            if cur is None:
                return
            cur = cur.next

        if cur is None:
            return

        new_node = Node(data)
        new_node.next = cur.next
        cur.next = new_node

    def set(self, index, data):
        cur = self.head
        for _ in range(index):
            if cur is None:
                return
            cur = cur.next

        if cur is None:
            return

        cur.data = data

    def is_empty(self):
        return self.head is None

    def stringify(self):
        elements = []
        cur_node = self.head
        while cur_node:
            elements.append(str(cur_node.data))
            cur_node = cur_node.next
        return "->".join(elements)

    def size(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count
