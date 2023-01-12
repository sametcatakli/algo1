import math

a_input = input('tyoe value of a: ')
b_input = input('type value of b: ')
c_input = input('type value of c: ')


def racine(a, b, c):
    if b > 0 and c > 0:
        equation = str(a) + 'x² +' + str(b) + 'x +' + str(c)
    elif b > 0 and c < 0:
        equation = str(a) + 'x² +' + str(b) + 'x ' + str(c)
    else:
        equation = str(a) + 'x² ' + str(b) + 'x ' + str(c)

    delta = (b**2) - 4 * (a * c)
    if delta > 0:
        x_1 = (-b + math.sqrt(delta)) / 2 * a
        x_2 = (-b - math.sqrt(delta)) / 2 * a
        print('Les racines pour la fonction ', equation ,' sont: ', x_1, x_2)
    elif delta == 0:
        x = -b / 2 * a
        print('La racine pour la fonction', equation ,' est:', x)
    else:
        print('Pas de solution')


racine(int(a_input), int(b_input), int(c_input))
