

def is_prime (n):

    if n == 1:
        #print('1 is special')
        return False
    for x in range (2, n):
        if n % x == 0:
            #print('{} equals {} x {}'.format(n, x, n // x))
            return False
    else:
        #print(n, 'is a prime number')
        return True




def primes_between (s, e):

    for n in range(s, e + 1):

        is_prime(n)



def count_primes_between (s, e):

    c  = 0

    for n in range (s, e + 1):

        if is_prime(n):
            c = c + 1

    print(c)