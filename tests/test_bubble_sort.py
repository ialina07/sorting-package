from src.sorting_algorithms import bubble_sort

def test_empty_list():
    assert bubble_sort([]) == []

def test_single_element():
    assert bubble_sort([5]) == [5]

def test_sorted_list():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_duplicate_elements():
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_negative_numbers():
    assert bubble_sort([-3, -1, -4, -2]) == [-4, -3, -2, -1]

def test_mixed_numbers():
    assert bubble_sort([3, -1, 0, -2, 5]) == [-2, -1, 0, 3, 5]
