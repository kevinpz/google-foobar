from solution import solution


#def test_solution_0():
#    assert solution([9]) == 9


def test_solution_1():
    assert solution([3, 1, 4, 1]) == 4311


def test_solution_2():
    assert solution([3, 1, 4, 1, 5, 9]) == 94311


def test_solution_3():
    assert solution([9, 9, 9, 9, 9, 9, 9, 9, 9]) == 999999999
