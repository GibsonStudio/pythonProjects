

def functionTest (input):

    return "(" + input + ")"




def count (n = 10):

    if n < 1:
        n = 1

    for i in range(1,n + 1):
        print(i)



class Animal():

    def __init__ (self, args = {}):
        self.type = args.get('type', 'dog')
        self.legs = args.get('legs', 4)
        self.canFly = args.get('canFly', False)

    def debug (self):
        m = 'A ' + self.type + ' has ' + str(self.legs) + ' legs and '
        if self.canFly:
            m += 'can fly.'
        else:
            m += 'CANNOT fly.'
        print(m)

