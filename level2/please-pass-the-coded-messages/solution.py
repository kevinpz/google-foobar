from itertools import combinations


def solution(l):
    # For each possible size, starting from the biggest
    for size in reversed(range(1, len(l) + 1)):
        res = []
        # Get all the possible combinations from the input and the current size
        for comp in combinations(l, size):
            # If the sum of all the digits is divisible by 3, the number is also divisible by 3
            if sum(comp) % 3 == 0:
                # Get the biggest number possible using all the current digit
                res.append((sorted(comp, reverse=True)))
        # And add the solution to the list
        res.sort(reverse=True)

        # If the list is not empty, return the first element as an int
        if res:
            return int("".join(map(str, res[0])))

    # There is no solution
    return 0
