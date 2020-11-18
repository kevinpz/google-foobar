from itertools import combinations


def solution(l):
    for size in reversed(range(1, len(l) + 1)):
        # check all the combinations possible for each size
        max_nb = 0
        for comb in combinations(l, size):
            # if the sum of all the digits is a multiple of 3, then all the numbers combination will be
            if sum(comb) % 3 == 0:
                max_nb = max(max_nb, int(''.join(map(str, sorted(comb, reverse=True)))))

        if max_nb:
            return max_nb

    return 0


if __name__ == '__main__':
    assert solution([3, 1, 4, 1]) == 4311
    assert solution([3, 1, 4, 1, 5, 9]) == 94311
