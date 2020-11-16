class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.contents = [Node(None, None) for _ in range(self.capacity)]


