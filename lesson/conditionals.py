

a, b = 10, 1

if a < b:
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('a ({}) is greater than b ({})'.format(a, b))


print(a if a < b else b)