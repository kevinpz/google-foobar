def answer(xs):
    xs.sort()
    negative_nb =  [n for n in xs if n < 0]
    positive_nb =  [n for n in xs if n > 0]

    if len(negative_nb) % 2 == 1 and len(positive_nb) > 0:
        negative_nb.pop()

    nb = negative_nb + positive_nb
    res = 1

    if len(nb) == 0:
        res = 0

    for n in nb:
        res *= n

    if res < 0 and 0 in xs:
        res = 0

    return str(res)

def check_solution(res, solution):
    print(res)
    print(solution)
    print(res == solution)

if __name__ == "__main__":

    input = [2, 0, 2, 2, 0]
    output = "8"
    res = answer(input)
    check_solution(res, output)

    input = [-2, -3, 4, -5]
    output = "60"
    res = answer(input)
    check_solution(res, output)

    input = [0]
    output = "0"
    res = answer(input)
    check_solution(res, output)

    input = [-1]
    output = "-1"
    res = answer(input)
    check_solution(res, output)

    input = [-1, 0]
    output = "0"
    res = answer(input)
    check_solution(res, output)
