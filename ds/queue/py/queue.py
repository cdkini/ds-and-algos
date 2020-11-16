class Node:
  def __init__(self, val=0, prev=None, next=None):
    self.val = val
    self.prev = prev
    self.next = next


class Queue:
  def __init__(self):
    self.size = 0
    self.dummy_head = Node()
    self.dummy_tail = Node()
    self.dummy_head.next = self.dummy_tail
    self.dummy_tail.prev = self.dummy_head
    
  def enqueue(self, val):
    node = Node(val)
    temp = self.dummy_tail.prev
    self.dummy_tail.prev = node
    node.next = self.dummy_tail
    node.prev = temp
    node.prev.next = node
    self.size += 1
    
  def dequeue(self):
    if self.is_empty():
      raise Exception("Cannot dequeue an empty Queue")
    res = self.dummy_head.next.val
    self.dummy_head.next = self.dummy_head.next.next
    self.dummy_head.next.prev = self.dummy_head
    self.size -= 1
    return res
      
  def peek(self):
    if self.is_empty():
      raise Exception("Cannot peek an empty Queue")
    return self.dummy_head.next.val
    
  def display(self):
    if self.is_empty():
      print([])
    curr = self.dummy_head.next
    contents = []
    for _ in range(self.size):
        contents.append(curr.val)
        curr = curr.next
    print(contents)
    return contents

  def is_empty(self):
    return not self.size
    
  def size(self):
    return self.size

q = Queue()
for n in range(1,6):
    q.enqueue(n)
    
q.display()
