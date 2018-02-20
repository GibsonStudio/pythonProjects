

#import gui
#import include



class Animal:

    def __init__(self, args = {}):

        self.species = args['species'] if 'species' in args else 'dog'
        self.legs = args['legs'] if 'legs' in args else 4
        self.color = args['color'] if 'color' in args else 'white'

    def info(self):
        txt = 'This is a ' + self.color + ' ' + self.species + '. ' + self.species + 's have ' + str(self.legs) +' legs.'
        print(txt)

d = Animal({'species':'cat', 'legs':2, 'color':'black'})

print(d.species)
d.info()

