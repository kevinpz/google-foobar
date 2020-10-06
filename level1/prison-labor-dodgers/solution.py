def solution(x, y):
    return set(x).symmetric_difference(set(y)).pop()


if __name__ == '__main__':
    assert solution([13, 5, 6, 2, 5], [5, 2, 5, 13]) == 6
    assert solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]) == -4
