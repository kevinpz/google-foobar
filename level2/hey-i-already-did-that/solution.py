def base_subtraction(x, y, b):
    """
    Subtract two numbers in base b like we do it manually on paper
    So there's no need to convert from base b to base 10, and reconvert the number to base b again

    :param x: number x
    :param y: number y
    :param b: base b
    :return: the subtraction of the 2 number in base b as string
    """
    # Used to carry if the botom number is greater than the top number
    rem = 0
    res = ''
    # For each number starting with the smallest value (right)
    for pos in reversed(range(len(x))):
        # Get the int of the top number
        cx = int(x[pos])
        # Get the int of the bottom number + rem from previous number
        cy = int(y[pos]) + rem
        # Do the subtraction with modulo to stay in base b
        res = str((cx - cy) % b) + res

        # If the bottom number is greater than the top one, we need to add a 1 remaining for the next number
        if cy > cx:
            rem = 1
        else:
            rem = 0

    # Return the result in string format
    return res


def solution(n, b):
    minion_list = []
    # Get the list len
    k = len(n)

    # Until we find the same minion id again
    while n not in minion_list[:-1]:
        # Get X
        x = ''.join(sorted(n, reverse=True))
        # Get Y
        y = ''.join(sorted(n))
        # Get the difference between both number in base b
        z = base_subtraction(x, y, b).zfill(k)
        # Add the minion id
        minion_list.append(z)
        n = z

    # The result is the difference between the 2 position of the same minion id
    return len(minion_list) - minion_list.index(n) - 1
