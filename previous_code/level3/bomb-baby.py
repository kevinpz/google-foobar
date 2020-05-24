def solution(mach_nb, facula_nb):
    mach_nb = int(mach_nb)
    facula_nb = int(facula_nb)

    res = 0

    while mach_nb > 1 and facula_nb > 1:

        if mach_nb > facula_nb:
            res += (mach_nb // facula_nb)
            mach_nb %= facula_nb
        else:
            res += (facula_nb // mach_nb)
            facula_nb %= mach_nb

    if mach_nb < 1 or facula_nb < 1:
        res = "impossible"
    else:
        res += (max(mach_nb, facula_nb) - 1)

    return str(res)


if __name__ == "__main__":
    problems = []
    problems.append(["4", "7", "4"])
    problems.append(["2", "1", "1"])
    problems.append(["2", "4", "impossible"])

    for mach_nb, facula_nb, sol in problems:
        answer = solution(mach_nb, facula_nb)
        print("Sol = {}\nAnswer = {}".format(sol, answer))
        assert sol == answer
