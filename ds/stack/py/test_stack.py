from stack import Stack

def test_is_empty():
    s = Stack()
    assert s.empty()

def test_is_not_empty():
    s = Stack()
    s.push(1)
    assert not s.empty()

def test_peek_on_empty():
    s = Stack()
    assert not s.peek()

def test_valid_peek():
    s = Stack()
    s.push(1)
    assert s.peek() == 1
    assert not s.empty()

def test_pop_on_empty():
    s = Stack()
    assert not s.pop()

def test_valid_pop():
    s = Stack()
    s.push(1)
    assert s.pop() == 1
    assert s.empty()

def test_push():
    s = Stack()
    for i in range(10):
        s.push(i)
        assert len(s.contents) == i + 1

def test_not_found_search():
    s = Stack()
    for i in range(10):
        s.push(i)
    assert not s.search(12)

def test_valid_search():
    s = Stack()
    for i in range(11):
        s.push(i)
    assert s.search(10) == 1
    assert s.search(6) == 5
    assert s.search(1) == 10
