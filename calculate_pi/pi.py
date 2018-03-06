import math

def calculate_gregory_leibniz (iterations = 10):

    #at 2,000,000 iterations, accurate to 6 dp
    pi = 0

    for n in range(1, iterations + 1):

        inc = 4 / ( (n * 2) - 1 )

        if (n % 2) == 0:

            pi = pi - inc

        else:

            pi = pi + inc

    return pi



def calculate_nilakantha (iterations = 10):

    pi = 3;

    for n in range(2, iterations + 1):

        index = (n * 2) - 2
        inc = 4 / (index * (index + 1) * (index + 2))

        if (n % 2) == 0:

            pi = pi + inc

        else:

            pi = pi - inc

    return pi







def test_gregory_leibniz (iterations = 10):

    pi = math.pi
    script = calculate_gregory_leibniz(iterations)
    print('Python: ' + str(pi))
    print('Script: ' + str(script))
    print('Differ: ' + show_difference(pi, script))



def test_nilakantha (iterations = 10):

    pi = math.pi
    script = calculate_nilakantha(iterations)
    print('Python: ' + str(pi))
    print('Script: ' + str(script))
    print('Differ: ' + show_difference(pi, script))



def show_difference (v1, v2):

    v1 = str(v1)
    v2 = str(v2)
    diff = ''

    length = len(v1)

    if len(v2) < length:
        length = len(v2)

    for n in range (0, length):

        if v1[n] != ".":
            this_diff = math.fabs(int(float(v1[n])) - int(float(v2[n])))
            this_diff = math.floor(this_diff)
            diff += str(this_diff)
        else:
            diff += v1[n]

    return diff

