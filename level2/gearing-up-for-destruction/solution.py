"""
Trying to solve it with a mathematical equation.

Let's say we have the pegs [A, B, C, ..., M, N]
And we have all the gear with their radius [rA, rB, rC, ..., rM, rN]

And let's call the distance between the pegs as following:
A -> B = dAB
B -> C = dBC
...
M -> N = dMN

So we can write:
dAB = rA + rB
dBC = rB + rC
...
dMN = rM + rN

Also, we want the last gear to be half the first one, so we have:
rN = rA / 2

Let's now use lines combinations to remove the gear radius (adding or subtracting lines).
Depending if the list has an even or odd number of elements, the last sign will be different.

For an even number:
dAB - dBC + ... + dMN = rA + rB - rB - rC + ... + rM + rN 
With simplification:
dAB - dBC + ... + dMN = rA + ra/2
rA = 2/3 * (dAB - dBC + ... + dMN)

For an odd number:
dAB - dBC + ... - dMN = rA + rB - rB - rC + ... - rM - rN 
With simplification:
dAB - dBC + ... - dMN = rA - ra/2
rA = 2 * (dAB - dBC + ... - dMN)

Now we need to check that all the other gears have a size >= 1, otherwise the solution is not possible.
"""

from fractions import Fraction


def solution(pegs):
    # Get the denominator based on the list parity
    if len(pegs) % 2 == 0:
        frac = 3
    else:
        frac = 1

    # Initiate the sum and the multiplicator
    p_sum = 0
    mul = 1

    # Calculate the sum of distance between the pegs
    for i in range(0, len(pegs) - 1):
        p_sum += mul * (pegs[i + 1] - pegs[i])
        mul *= -1

    # Get the value as a fraction
    rA = Fraction(2 * p_sum, frac)

    # If the first gear is too small, the last one will be below 1
    if rA < 2:
        return [-1, -1]

    current_gear_size = rA
    # Check if all the other gear sizes are greater or equal to 1
    for i in range(0, len(pegs) - 2):
        current_gear_size = pegs[i + 1] - pegs[i] - current_gear_size
        if current_gear_size < 1:
            return [-1, -1]

    return [rA.numerator, rA.denominator]


if __name__ == '__main__':
    assert solution([4, 30, 50]) == [12, 1]
    assert solution([4, 17, 50]) == [-1, -1]
