

def nums(n):
    while (True):
        yield n
        n = n + 1



for x in nums(0):
    if x > 10: break
    print(x)