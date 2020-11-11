from cyclic_sort import cyclic_sort

def test_cyclic_sort_on_empty_arr():
    assert cyclic_sort([]) == []

def test_cyclic_sort_on_len_one_arr():
    assert cyclic_sort([1]) == [1]

def test_cyclic_sort():
    assert cyclic_sort([7, 4, 5, 2, 6, 1, 3, 0]) == [0, 1, 2, 3, 4, 5, 6, 7]
