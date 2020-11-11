import pytest
from binary_search import binary_search

def test_invalid_input():
    assert binary_search([], 1) == -1
    assert binary_search(None, 1) == -1

def test_element_not_found():
    assert binary_search([1, 2, 6, 7, 8, 9, 11, 13], 23) == -1

def test_element_found():
    assert binary_search([1, 3, 5, 7, 11, 13, 14], 5) == 2

def test_first_occurence_found():
    assert binary_search([3, 3, 3, 5, 7, 8, 9, 11, 12], 3) == 1
