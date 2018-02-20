


class AnimalActions:

    def bark(self): return self._doAction('bark')
    def fur(self): return self._doAction('fur')
    def wings(self): return self._doAction('wings')
    def legs(self): return self._doAction('legs')


    def _doAction(self, action):

        if action in self.strings:
            print(self.strings[action])
        else:
            print('The {} has no {}'.format(self.animalName(), action))


    def animalName (self):
        return self.__class__.__name__.lower()




class Dog (AnimalActions):

    strings = dict(
        bark = 'Woof!!',
        fur = 'Thick fur',
        legs = 'Has 4 legs'
    )



class Bird (AnimalActions):

    strings = dict(
        wings = 'Has 2 wings',
        legs = 'Has 2 legs'
    )



b = Bird()
d = Dog()

try:
    b.wing()
except Exception as e:
    print('oops ({})'.format(e))
