from fractions import Fraction

# find the least common multiple in a given list
def find_lcm(mylist):
    max_val = max(mylist)
    cpt, common = 0, 0
    rest = sum(mylist)
    # until we find a common multiple
    while (rest != 0):
        cpt += 1
        # we increase the current number
        common = cpt * max_val
        rest = sum([common % v if v > 0 else 0 for v in mylist])

    return common


# once we have the result; we can find the LCM and put a common denominator for all final states probas
def normalize_res(compute_m, terminal_state_nb):
    den_list = [compute_m[i].denominator for i in range(terminal_state_nb)]
    lcm = find_lcm(den_list)
    res = [compute_m[i].numerator * lcm / den_list[i] for i in range(terminal_state_nb)]
    res.append(lcm)
    return res


# Use Gaussian elimination simplified for our case as we know that the matrix can be inversed
def inverse_m(m, size):
    # create an identify matrix, it will have the same operations that our matrix to get the inverse
    idy = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    # for each line
    for i in range(size):
        # we get our factor
        factor = m[i][i]
        for j in range(size):
            # we normalize our line
            m[i][j] /= factor
            idy[i][j] /= factor

        # for the other lines
        for x in range(size):
            if (x != i):
                # we use our pivot to have a 0
                factor = m[x][i]
                for k in range(size):
                    m[x][k] -= factor * m[i][k]
                    idy[x][k] -= factor * idy[i][k]
    return idy


# reorder matrix, put empty row at the bottom, and reorder the colomn as well
def reorder_m(m, size, transition_state_nb):
    # get the position of transition states and final states
    trans_order = [i for i in range(size) if sum(m[i]) > 0]
    final_order = [i for i in range(size) if sum(m[i]) == 0]
    ordered_list = trans_order + final_order

    # init a new array
    ordered_m = [[0 for j in range(size)] for i in range(size)]

    # for each transition row, we rearrange them
    for i in range(transition_state_nb):
        for j in range(size):
            ordered_m[i][j] = m[ordered_list[i]][ordered_list[j]]

    return ordered_m


# from the original matrix, we create a proba matrix
def create_proba_m(m, size, transition_state_nb):
    # get the sum for each row
    sum_by_row = [sum(m[i]) for i in range(size)]

    proba_m = []
    for i in range(size):
        # if we are on transition states
        if i < transition_state_nb:
            proba_m.append([Fraction(m[i][x], sum_by_row[i]) for x in range(size)])
        # if we are on stable states
        else:
            proba_m.append([Fraction(1) if i == x else Fraction(0) for x in range(size)])
    return proba_m


# we use the markov algorithm with absorbing states
def compute_proba(proba_m, size, terminal_state_nb, transition_state_nb):
    # we cut our matrix in 4 different parts
    q = [[proba_m[i][j] for j in range(transition_state_nb)] for i in range(transition_state_nb)]
    r = [[proba_m[i][j] for j in range(transition_state_nb, size)] for i in range(transition_state_nb)]
    idy = [[1 if i == j else 0 for j in range(transition_state_nb)] for i in range(transition_state_nb)]
    iq = [[idy[i][j] - q[i][j] for j in range(transition_state_nb)] for i in range(transition_state_nb)]

    # n = gauss(iq, idy)
    n = inverse_m(iq, transition_state_nb)
    # n = inv(iq)
    # the proba states are given by B = NR
    b = [sum([n[0][y] * r[y][x] for y in range(transition_state_nb)]) for x in range(terminal_state_nb)]

    return b


def solution(m):
    size = len(m)
    # number of stable states
    terminal_state_nb = sum([1 if sum(m[i]) == 0 else 0 for i in range(size)])
    # number of transition states
    transition_state_nb = size - terminal_state_nb

    if (transition_state_nb > 0):
        order_m = reorder_m(m, size, transition_state_nb)
        proba_m = create_proba_m(order_m, size, transition_state_nb)
        compute_m = compute_proba(proba_m, size, terminal_state_nb, transition_state_nb)
        res = normalize_res(compute_m, terminal_state_nb)
    else:
        res = [1, 1]

    return res


if __name__ == "__main__":
    problems = []

    m = [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    problems.append([m, [7, 6, 8, 21]])

    m = [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    problems.append([m, [0, 3, 2, 9, 14]])

    m = [
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    problems.append([m, [1, 2, 3]])

    m = [
        [0]
    ]
    problems.append([m, [1, 1]])

    m = [
        [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
        [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
        [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
        [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    problems.append([m, [1, 2, 3, 4, 5, 15]])

    m = [
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    problems.append([m, [4, 5, 5, 4, 2, 20]])

    m = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    problems.append([m, [1, 1, 1, 1, 1, 5]])

    m = [
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    problems.append([m, [2, 1, 1, 1, 1, 6]])

    m = [
        [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
        [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
        [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    problems.append([m, [6, 44, 4, 11, 22, 13, 100]])

    m = [
        [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
        [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
        [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    problems.append([m, [1, 1, 1, 2, 5]])

    for pb, sol in problems:
        answer = solution(pb)
        print("Sol = {}\nAnswer = {}".format(sol, answer))
        assert sol == answer
