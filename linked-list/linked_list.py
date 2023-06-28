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
            return None
        value = self.tail.value
        if self.tail.prev == None:
            self.head = self.tail = None
            self.empty = True
        else:
            self.tail = self.tail.prev

        return value

    def unshift(self, value):
        if self.empty:
            self.push(value)
        else:
            self.head.prev = Node(value, self.head, None)
            self.head = self.head.prev        

    def shift(self):
        if self.empty:
            return None
        value = self.head.value
        if self.head.next == None:
            self.head = self.tail = None
            self.empty = True
        else:
            self.head = self.head.next
        return value
