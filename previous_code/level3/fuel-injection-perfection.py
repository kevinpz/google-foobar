def solution(nb_str):
    nb = int(nb_str)
    step_nb = 0
    while nb != 1:
        if nb % 2 == 0:
            nb /= 2
        elif (nb + 1) % 4 == 0 and nb > 4:
            nb += 1
        else:
            nb -= 1
        step_nb += 1

    return step_nb

if __name__ == "__main__":
    problems = []
    problems.append(["15", 5])
    problems.append(["4", 2])
    problems.append(["05777819831305312999125787224320065042244470089719186314415387201215456655136200322565740124329708779278797484041710399217457446805720661074872115467713819431446999622819160767611627549614355463457535865577623518900613980124146579765730510662839186912292084901023322536223274268874411448445075837135407", 1019])

    for pb, sol in problems:
        answer = solution(pb)
        print("Sol = {}\nAnswer = {}".format(sol, answer))
        assert sol == answer
