def solution(l):
    res = 0
    # For each element, starting at position 1
    for pos in range(1, len(l) - 1):
        # Get the element value
        val = l[pos]
        # Get the list of all its dividers on the left side of the list
        dividers_nb = len([d for d in l[:pos] if val % d == 0])
        # Get the list of all its multiples on the right side of the list
        multiples_nb = len([m for m in l[pos + 1:] if m % val == 0])
        # Calculate the combination number
        res += dividers_nb * multiples_nb
    return resw
