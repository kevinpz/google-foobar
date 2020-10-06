def solution(x, y):
    # Convert to int
    x = int(x)
    y = int(y)

    answer = 0

    # Until we have a bomb at 1 or below
    while x > 1 and y > 1:
        x, y = max(x, y), min(x, y)
        # How much time we can have y in x
        answer += x // y
        # What is the remaining for the new x
        x %= y

    # If one value is below 1 it's impossible
    if x < 1 or y < 1:
        answer = 'impossible'

    # If one value is above 1, we just have to compute how much to reach 1
    elif x > 1 or y > 1:
        answer += max(x, y) - 1

    return str(answer)
