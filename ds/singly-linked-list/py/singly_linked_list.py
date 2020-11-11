class Node:
    def __init__(self, val, next_node):
        self.val = val
        self.next = next_node

class SLList:
    def __init__(self):
        self.__sentinel = Node(float('inf'), None)
        self.__size = 0

    def append(self, item):
        ptr = self.__sentinel
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(item, None)
        self.__size += 1

    def insert(self, item, index):
        pass # TODO: Open to implement!

    def clear(self):
        self.__init__()

    def contains(self, item):
        ptr = self.__sentinel.next
        while ptr:
            if ptr.val == item:
                return True
            ptr = ptr.next
        return False

    def get(self, index):
        if index >= self.__size:
            return None
        ptr = self.__sentinel.next
        for _ in range(index):
            ptr = ptr.next
        return ptr.val

    def index_of(self, item):
        i = 0
        ptr = self.__sentinel.next
        while ptr:
            if ptr.val == item:
                return i
            ptr = ptr.next
            i += 1
        return -1

    def is_empty(self):
        return not self.__size

    def remove_index(self, index):
        pass # TODO: Open to implement!

    def remove_item(self, item):
        pass # TODO: Open to implement!

    def remove_all(self, item):
        pass # TODO: Open to implement!

    def sort(self):
        pass # TODO: Open to implement!

    @property
    def size(self):
        return self.__size

