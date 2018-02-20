import math

def get_nth (n = 0):

    phi = (1 + math.sqrt(5)) / 2
    thi = 1 - phi

    fib = (math.pow(phi,n) - math.pow(thi, n)) / math.sqrt(5)

    return math.ceil(fib - (fib % 1))





def get_sequence (start = 0, end = 10):

    sequence = []

    for n in range(start, end + 1):

        number = get_nth(n)
        sequence.append(number)

    return sequence



def get_simple_sequence (end = 10):

    if end < 1:
        end = 1

    sequence = [0,1]

    n = 2

    while n <= end:

        next_number = sequence[n-2] + sequence[n-1]
        sequence.append(next_number)
        n += 1

    return sequence

