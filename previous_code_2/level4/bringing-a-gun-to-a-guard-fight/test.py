from solution import solution


def test_solution_1():
    assert solution([3, 2], [1, 1], [2, 1], 4) == 7


def test_solution_2():
    assert solution([300, 275], [150, 150], [185, 100], 500) == 9
