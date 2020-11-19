def solution(n):
    n = int(n)
    res = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            if (n + 1) % 4 == 0 and n > 3:
                n += 1
            else:
                n -= 1
        res += 1

    return res


if __name__ == '__main__':
    assert solution('15') == 5
    assert solution('4') == 2