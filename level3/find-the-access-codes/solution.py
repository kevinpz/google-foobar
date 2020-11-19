def solution(l):
    res = 0
    for i in range(1, len(l) - 1):
        left_nb = len([x for x in l[:i] if l[i] % x == 0])
        right_nb = len([x for x in l[i + 1:] if x % l[i] == 0])
        res += left_nb * right_nb

    return res


if __name__ == '__main__':
    assert solution([1, 2, 3, 4, 5, 6]) == 3
    assert solution([1, 1, 1]) == 1