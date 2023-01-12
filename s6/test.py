import random
from random import *

bag = [['1'], ['2'], ['3'], ['4']]
shuffle(bag, random)
bag.pop()
random_el = randrange(0, 2)
random_add = bag[random_el].copy()
bag.append(random_add)


for i in range(len(bag)):
    bag[i].append(randrange(1, 3))

print(bag)
jeu = bag.copy()


def peut_retirer(i, bag, jeu):
    given = [i]
    if given in bag:
        if given in jeu:
            for k in jeu:
                if jeu[i][0] == i:
                    return True
                else:
                    return False


print(peut_retirer(3, bag, jeu))
