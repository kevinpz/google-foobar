# Using the Absorbing Markov Chains to compute the probability
# https://youtu.be/qhnFHnLkrfA

from fractions import Fraction, gcd
from functools import reduce


def get_frac_matrix(matrix, m_size, transition_state_nb):
    """
    Transform a matrix to use Fraction for each element

    :param matrix: the matrix to transform
    :param m_size: the number of column
    :param transition_state_nb: the number of lines
    :return: a matrix with Fraction elements
    """
    # get the sum for each row so we can use it for fraction
    sum_by_row = [sum(matrix[i]) for i in range(transition_state_nb)]

    frac_m = []

    for i in range(transition_state_nb):
        frac_m.append([Fraction(matrix[i][j], sum_by_row[i]) for j in range(m_size)])

    return frac_m


def get_reorg_matrix(m, m_size, transition_state_nb):
    """
    Reorder the matrix to only keep the rows with the transition states
    By storing the new order in an array, we can have a mapping between new pos (idx) and old pos (value)
    For example reorg_states = [2,3,1,0] means the first new row/col was in position 2 before, and so on...

    :param m: the original matrix
    :param m_size: the original matrix size
    :param transition_state_nb: the number of transision states
    :return: a QR matrix of the size transition_state_nb*m_size (because we have the transition states first here)
    """

    # Get the new position for the transision and the final states
    transition_states = [i for i in range(m_size) if sum(m[i]) > 0]
    final_states = [i for i in range(m_size) if sum(m[i]) == 0]
    reorg_states = transition_states + final_states

    # Init an empty matrix  the same size of RQ
    reorg_m = [[0 for _ in range(m_size)] for _ in range(transition_state_nb)]

    # for each transition row, we rearrange them
    for i in range(transition_state_nb):
        for j in range(m_size):
            reorg_m[i][j] = m[reorg_states[i]][reorg_states[j]]

    return reorg_m


# Use Gaussian elimination simplified for our case as we know that the matrix can be inversed
def get_inverse_matrix(matrix, size):
    """
    Since we cannot use numpy, we need to do the matrix inversion
    Use Gaussian elimination simplified for our case as we know that the matrix can be inversed

    :param matrix: the matrix to be inverted
    :param size: the matrix size
    :return: the inverted matrix
    """
    # create an identify matrix, it will have the same operations that our matrix to get the inverse
    idy = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    # for each line
    for i in range(size):
        # we get our factor
        factor = matrix[i][i]
        for j in range(size):
            # we normalize our line
            matrix[i][j] /= factor
            idy[i][j] /= factor

        # for the other lines
        for x in range(size):
            if (x != i):
                # we use our pivot to have a 0
                factor = matrix[x][i]
                for k in range(size):
                    matrix[x][k] -= factor * matrix[i][k]
                    idy[x][k] -= factor * idy[i][k]
    return idy


def get_proba_matrix(matrix, m_size, transition_state_nb, terminal_state_nb):
    """
    Calculate the probability for the matrix

    :param matrix: the QR matrix to transform
    :param m_size: the number of column
    :param transition_state_nb: the number of lines
    :return: a probability matrix for each element
    """
    # We need to cut our matrix to get the R and the Q matrix
    q_matrix = [[matrix[i][j] for j in range(transition_state_nb)] for i in range(transition_state_nb)]
    r_matrix = [[matrix[i][j] for j in range(transition_state_nb, m_size)] for i in range(transition_state_nb)]

    # To find the probability matrix, we need to find the FR matrix, with F = (I - Q) ^ -1
    # So let's create an identity matrix of the same size than Q first
    id_matrix = [[1 if i == j else 0 for j in range(transition_state_nb)] for i in range(transition_state_nb)]

    # Now we calculate I - Q
    iq_matrix = [[id_matrix[i][j] - q_matrix[i][j] for j in range(transition_state_nb)] for i in range(transition_state_nb)]

    # And we need to invert it
    f_matrix = get_inverse_matrix(iq_matrix, transition_state_nb)

    # the proba states are given by FR, only use the row 0 because we want the final states
    proba_list = [sum([f_matrix[0][y] * r_matrix[y][x] for y in range(transition_state_nb)]) for x in range(terminal_state_nb)]

    return proba_list


def find_lcm(denominators):
    """
    Find the LCM from a integer list

    :param denominators: integer list
    :return: the LCM value
    """
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)


def normalize_res(proba_matrix, terminal_state_nb):
    """
    Normalize the result with a common denominator for all the states

    :param proba_matrix: the probability matrix
    :param terminal_state_nb: number of terminal states
    :return: the normalized matrix
    """
    # List all denominator for each state
    den_list = [proba_matrix[i].denominator for i in range(terminal_state_nb)]
    # Find the least common multiple in the denominator list
    lcm = find_lcm(den_list)
    # Convert the list to have the LCM
    res = [proba_matrix[i].numerator * lcm / den_list[i] for i in range(terminal_state_nb)]
    # Add it at the end
    res.append(lcm)
    return res


def solution(m):
    # We want to reorganize the matrix to the following format:
    #     |QR|
    # P = |  |
    #     |OI|

    m_size = len(m)
    # number of stable states
    terminal_state_nb = sum([1 if sum(m[i]) == 0 else 0 for i in range(m_size)])
    # number of transition states
    transition_state_nb = m_size - terminal_state_nb

    if transition_state_nb > 0:
        # I and O are identity matrix and null matrix, we don't really need to keep them, we only need QR to compute the proba
        qr_matrix = get_reorg_matrix(m, m_size, transition_state_nb)

        # Now we have the QR matrix, we need to convert it to fraction, so it's easier for the computation
        qr_frac_matrix = get_frac_matrix(qr_matrix, m_size, transition_state_nb)

        # Get the probability matrix
        proba_list = get_proba_matrix(qr_frac_matrix, m_size, transition_state_nb, terminal_state_nb)

        # Normalize the result to have the right output
        res = normalize_res(proba_list, terminal_state_nb)
    else:
        res = [1, 1]

    return res
