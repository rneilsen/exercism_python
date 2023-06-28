class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.prev = previous


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.empty = True

    def push(self, value):
        if self.empty:
            self.empty = False
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next

    def pop(self):
        if self.empty:
            raise IndexError("Cannot pop from an empty list")
        value = self.tail.value
        if self.tail.prev == None:
            self.head = self.tail = None
            self.empty = True
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value

    def unshift(self, value):
        if self.empty:
            self.push(value)
        else:
            self.head.prev = Node(value, self.head, None)
            self.head = self.head.prev        

    def shift(self):
        if self.empty:
            raise IndexError("Cannot pop from an empty list")
        value = self.head.value
        if self.head.next == None:
            self.head = self.tail = None
            self.empty = True
        else:
            self.head = self.head.next
            self.head.prev = None
        return value

    def delete(self, value):
        if self.empty:
            raise ValueError("Cannot delete from an empty list")
        cur_node = self.head
        while cur_node:
            if cur_node.value == value:
                if cur_node.next is None and cur_node.prev is None:
                    # deleting the only node
                    self.head = self.tail = None
                    self.empty = True
                elif cur_node.prev is not None and cur_node.next is not None:
                    # deleting from middle
                    cur_node.prev.next = cur_node.next
                    cur_node.next.prev = cur_node.prev
                elif cur_node.prev is not None and cur_node.next is None:
                    # deleting tail node
                    self.tail = cur_node.prev
                    self.tail.next = None
                elif cur_node.prev is None and cur_node.next is not None:
                    # deleting head node
                    self.head = cur_node.next
                    self.head.prev = None
                return
            cur_node = cur_node.next
        raise ValueError("Value not found")

    def __len__(self):
        length = 0
        cur_node = self.head
        while cur_node:
            length += 1
            cur_node = cur_node.next
        return length
