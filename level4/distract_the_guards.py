#!/usr/bin/env python2.7

class Guard():
    def __init__(self, number, banana):
        self.number = number
        self.banana = banana
        self.affected = False
        self.pair = None
        self.good_match = []
        self.match_nb = 0

    def check_match_possible(self, guard, power_tab):
        if self.number == guard.number:
            return False
        if self.banana == guard.banana:
            return False

        banana_gcd = gcd(self.banana, guard.banana)
        value = self.banana / banana_gcd + guard.banana / banana_gcd

        if value in power_tab:
            return False

        return True

    def add_match(self, guard):
        self.good_match.append(guard)
        self.match_nb += 1

    def affect_guard(self, guard):
        self.affected = True
        self.pair = guard.number
        guard.affected = True
        guard.pair = self.number

    def __str__(self):
        return "Number: {} Banana: {} Affected: {} Match nb: {} Match list: {} Pair is {}".format(self.number, self.banana, self.affected, self.match_nb, self.good_match, self.pair)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def init_power_two():
    # init a tab with the power of two to avoid recalculing each time
    power_tab = []
    val = 1
    for i in xrange(30):
        val *= 2
        power_tab.append(val)

    return power_tab

def init_guard(guard_nb, guard_list, banana_list):
    # init each guard with a number and banana numbers
    for i in xrange(guard_nb):
        my_guard = Guard(i, banana_list[i])
        guard_list.append(my_guard)

def match_guard(guard_nb, guard_list, power_tab):
    # for each guard
    for g1 in guard_list:
        # find all other guards that are matching
        for g2 in guard_list:
            if g1.check_match_possible(g2, power_tab):
                g1.add_match(g2)

def pick_guard(guard_nb, guard_list):
    # for each guard
    for g1 in guard_list:
        if not g1.affected:
            # try to find a guard that matches 
            for g2 in g1.good_match:
                if g2.affected:
                    continue
                else:
                    g1.affect_guard(g2)
                    break

def count_rem_guard(guard_list):
    res = sum([1 for g in guard_list if g.affected == False])
    return res


def answer(banana_list):
    power_tab = init_power_two()
    guard_nb = len(banana_list)
    guard_list = []

    banana_list.sort()

    # init our guard objects
    init_guard(guard_nb, guard_list, banana_list)
    # get the possible matches for each guard
    match_guard(guard_nb, guard_list, power_tab)

    # sort the list to have guards with fewer possibility at the begining
    guard_list.sort(key = lambda x: x.match_nb)

    # pick the better solution for each guard
    pick_guard(guard_nb, guard_list)
    # count how many guards are remaining
    res = count_rem_guard(guard_list)

    print(res)
    return res

    


banana_list = [1, 1]
answer(banana_list)
print('---> 2')

banana_list = [1, 7, 3, 21, 13, 19]
answer(banana_list)
print('---> 0')
