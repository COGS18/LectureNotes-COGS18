def test_divide_neighbors():
    assert type(divide_neighbors([1, 2])) == list
    assert divide_neighbors([1, 2, 4]) == [2, 2]


def test_sum_list():
    assert callable(sum_list)
    assert type(sum_list([1, 2, 3, 4])) == int
    assert sum_list([1, 2, 3, 4]) == 10