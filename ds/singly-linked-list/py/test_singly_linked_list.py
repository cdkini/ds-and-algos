from singly_linked_list import SLList

import pytest

def test_append():
    sll = SLList()
    for n in range(1, 10):
        sll.append(n)
        assert sll.to_arraylist()[-1] == n
        assert sll.size == n

def test_insert():
    sll = SLList()
    sll.insert('A', 0)
    sll.insert('B', 5)
    sll.insert('C', 0)
    sll.insert('D', 2)
    sll.insert('E', 3)
    assert sll.to_arraylist() == ['C', 'A', 'D', 'E', 'B']
    assert sll.size == 5

def test_clear():
    sll_one = SLList()
    sll_two = SLList()
    for n in range(1, 10):
        sll_two.append(n)
    assert sll_one.to_arraylist() != sll_two.to_arraylist()
    sll_two.clear()
    assert sll_one.to_arraylist() == sll_two.to_arraylist()

def test_contains():
    sll = SLList()
    assert not sll.contains(1)
    sll.append(1)
    assert sll.contains(1)

def test_get():
    sll = SLList()
    with pytest.raises(Exception):
        sll.get(4)
    for n in range(1, 10):
        sll.append(n)
    assert sll.get(4) == 5
    assert sll.get(11) == 9

def test_index_of():
    sll = SLList()
    for n in range(1, 10):
        sll.append(n)
    assert sll.index_of(6) == 5
    assert sll.index_of(32) == -1

def test_is_empty():
    sll = SLList()
    assert sll.is_empty()
    sll.append(1)
    assert not sll.is_empty()

def test_remove_by_index():
    sll = SLList()
    for i in range(10):
        sll.append(1)
    sll.remove_by_index(5)
    assert sll.size == 9
    sll.remove_by_index(15)
    assert sll.size == 8
