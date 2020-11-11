from merge_sort import merge_sort


def test_merge_sort_on_empty_arr():
    assert merge_sort([]) == []

def test_merge_sort_on_len_one_arr():
    assert merge_sort([1]) == [1]

def test_merge_sort_on_sorted_arr():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort():
    assert merge_sort([7,8,1,2,4,6,3,1,8,4,2,4]) == [1, 1, 2, 2, 3, 4, 4, 4, 6, 7, 8, 8]
