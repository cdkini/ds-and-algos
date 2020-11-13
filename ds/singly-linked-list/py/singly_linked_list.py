class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class SLList:
    def __init__(self):
        self.sentinel = Node(float("inf"), None)
        self.size = 0

    def append(self, item):
        node = Node(item, None)
        curr = self.sentinel
        while curr and curr.next:
            curr = curr.next
        curr.next = node
        self.size += 1

    def insert(self, item, index):
        node = Node(item, None)
        index = min(self.size, index)
        curr = self.sentinel
        i = 0
        while i != index:
            i += 1
            curr = curr.next
        temp = curr.next
        curr.next = node
        node.next = temp
        self.size += 1

    def clear(self):
        self.__init__()

    def contains(self, item):
        if self.is_empty():
            return False
        curr = self.sentinel.next
        while curr:
            if curr.val == item:
                return True
            curr = curr.next
        return False

    def get(self, index):
        if self.is_empty():
            raise Exception("Cannot retrieve elements from an empty list")
        index = min(self.size - 1, index)
        curr = self.sentinel.next
        i = 0
        while i != index:
            i += 1
            curr = curr.next
        return curr.val

    def index_of(self, item):
        curr = self.sentinel.next
        i = 0
        while curr:
            if curr.val == item:
                return i
            i += 1
            curr = curr.next
        return -1

    def is_empty(self):
        return not self.size

    def remove_by_index(self, index):
        if self.is_empty():
            return
        index = min(self.size - 1, index)
        curr = self.sentinel
        i = 0
        while i != index:
            i += 1
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1

    def remove_by_value(self, item):
        if self.is_empty():
            return False
        curr = self.sentinel
        while curr and curr.next:
            if curr.next.val == item:
                curr.next = curr.next.next
                self.size -= 1
                return True
            curr = curr.next
        return False

    def remove_all(self, item):
        if self.is_empty():
            return False
        item_removed = False
        curr = self.sentinel
        while curr and curr.next:
            while curr and curr.next and curr.next.val == item:
                curr.next = curr.next.next
                item_removed = True
                self.size -= 1
            curr = curr.next
        return item_removed

    def to_arraylist(self):
        res = []
        curr = self.sentinel.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
