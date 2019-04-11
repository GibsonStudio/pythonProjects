
import lib as l

print(l.functionTest("Hello World"))

animals = []

dog = l.Animal()
animals.append(dog)
cat = l.Animal({'type':'cat'})
animals.append(cat)
hawk = l.Animal({'type':'hawk', 'legs':2, 'canFly':True})
animals.append(hawk)


for a in animals:
    a.debug()







