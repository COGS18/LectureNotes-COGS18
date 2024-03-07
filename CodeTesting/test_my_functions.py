def test_divide_neighbors():
    assert type(divide_neighbors([1, 2])) == list
    assert divide_neighbors([1, 2, 4]) == [0.5, 0.5]
    assert divide_neighbors([2, 8, 4]) == [0.25, 2]

    # Test lists with not enough elements
    assert divide_neighbors([]) == []
    assert divide_neighbors([10]) == []
    
    # Test division by zero
    try:
        divide_neighbors([10, 0])
        assert False
    except ZeroDivisionError:
        "it passed"


def test_sum_list():
    # Check that sum_list is a function
    assert callable(sum_list)
    
    # Check that it returns an integer
    assert type(sum_list([1, 2, 3, 4])) == int

    # Check that it sums
    assert sum_list([1, 2, 3, 4]) == 10
    
    # Check that the sum of the empty list is 0
    assert sum_list([]) == 0