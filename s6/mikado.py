from random import *

bag = [0, 1, 2, 3]

bag_random = bag.copy()
shuffle(bag_random, random)


def creer_enchevetrements(bag, i, max):
    jeu = []
    if max <= len(bag) + 1:
        nbr = max
        for k in range(nbr):
            couple = (bag_random[k], i)
            jeu.append(couple)
            for j in range(len(jeu)):
                element1 = jeu[j][0]
                element2 = jeu[j][1]
                if element1 == element2:
                    jeu.pop(j)

    else:
        return "il n'y a pas autant de baguettes"
    return jeu


# print(creer_enchevetrements(bag, 8, 5))


def peut_retirer(i, bag, jeu):
    if i not in bag:
        return False
    for (i, j) in jeu:
        if i == j:
            return False
    return True


def creer_mikado(bag):
    res = []
    for i in bag:
        res += creer_enchevetrements(bag, i, len(bag) - 1)
    return res


# print(creer_mikado(bag))
# print(creer_mikado(bag))

def quel_ordre(bag, jeu):
    if jeu == []:
        return bag
    for baguette in bag:
        if peut_retirer(baguette, bag, jeu):
            sous_bag = bag[:]
            sous_bag.remove(baguette)
            sous_jeu = [c for c in jeu if baguette not in c]
            sous_ordre = quel_ordre(sous_bag, sous_jeu)
            if sous_ordre is None:
                return None
            else:
                return [baguette] + sous_ordre

    return None


jeu = creer_mikado(bag)
ordre = quel_ordre(bag, jeu)

print(ordre)
