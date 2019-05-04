def solution(size, elts):
    res = []
    max_val = 2 ** size - 1
    for elt in elts:

        # if the element is the root or higer, there is no solution
        if elt >= max_val:
            res.append(-1)
            continue

        # now we need to determine the closest subtree to reduce the size
        root = 1
        level = 1
        while root <= elt:
            root = root * 2 + 1
            level += 1

        # now we know the closest subtree, we're going to navigate to the right leaf until it becomes the root
        while root != elt:
            prev_root = root
            level -= 1
            if elt <= root - 2 ** level:
                root -= 2 ** level
            else:
                root -= 1

        res.append(prev_root)

    return res


if __name__ == "__main__":
    problems = []
    problems.append([3, [7, 3, 5, 1], [-1, 7, 6, 3]])
    problems.append([5, [19, 14, 28], [21, 15, 29]])

    for size, elts, sol in problems:
        answer = solution(size, elts)
        print("Sol = {}\nAnswer = {}".format(sol, answer))
        assert sol == answer
