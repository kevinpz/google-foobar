from functools import reduce


def solution(power_list):
    positive_list = []
    negative_list = []
    zero_in_list = False
    for elt in power_list:
        if elt > 0:
            positive_list.append(elt)
        elif elt < 0:
            negative_list.append(elt)
        else:
            zero_in_list = True

    negative_list.sort()
    if len(negative_list) % 2 == 1 and (len(positive_list) > 0 or zero_in_list):
        negative_list.pop()

    sum_list = positive_list + negative_list

    if len(sum_list) > 0:
        res = reduce(lambda x, y: x * y, sum_list)
    else:
        res = 0

    return str(res)


if __name__ == "__main__":
    problems = []
    problems.append([[2, 0, 2, 2, 0], "8"])
    problems.append([[-2, -3, 4, -5], "60"])
    problems.append([[0], "0"])
    problems.append([[-1], "-1"])
    problems.append([[-1, 0], "0"])

    for power_list, sol in problems:
        answer = solution(power_list)
        print("Solution = {}\nAnswer = {}".format(sol, answer))
        assert sol == answer
