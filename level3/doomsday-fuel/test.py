from solution import solution


def test_solution_1():
    assert solution([[0, 2, 1, 0, 0],
                     [0, 0, 0, 3, 4],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0]]
                    ) == [7, 6, 8, 21]



def test_solution_2():
    assert solution([[0, 1, 0, 0, 0, 1],
                     [4, 0, 0, 3, 2, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]
                    ) == [0, 3, 2, 9, 14]