def somme1(n):
    if n == 0:
        return 0
    else:
        return somme1(n-1)+n 
        #il manquait le return après le else


def somme2(n):
    if n == 0:
        return 0
    else:
        return somme2(n-1)+n #il faut passer n-1 comme argument à la fonction


def somme3(n): # fonctionne bien, pas de problème
    if n == 0:
        return 0
    else:
        return n+somme3(n-1)


def somme4(n):
    if n == 0:
        res = 0
    else:
        res =  somme4(n-1)+n # il faut ajouter le -1 à l'argument n quand on appel la fonction / il faut initier une variable res qui prend comme valeur le resultat de la fonction appelée sinon on peut pas le recuperer quand on fait return res
    return res # erreur d'indentation, il faut mettre le return en dehors de else sinon ça retourne pas le res du cas de base


def somme5(n):
    if n == 0: # il faut gerer le cas où n vaut 0, car si n vaut 0 la bloucle ne s'arrete jamais et compte tout les nombres négatifs => max recursion
        return 0
    else:
        return somme5(n-1)+n


print(somme5(3))
