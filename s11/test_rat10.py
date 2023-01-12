""" Devrait afficher dans la console:
1/3
11/5
3
Cannot create a rational from this str: Hello
Cannot create a rational from this str: 1/deux
"""

""" Note:
Pour convertir un str en Rational:
    - on supprime d'abord les blancs
    - on suppose ensuite qu'un des 3 formats suivants est utilise:
       n/d
       n
       f
    ou n et d sont des entiers et f est un float

    Les seuls caracteres acceptes sont donc les chiffres de 0 a 9
    et les caracteres '/' (slash) et '.' (point)
"""

from rational import Rational

print(Rational('1 / 3'))
print(Rational(' 2.2'))
print(Rational('3 '))
try:
    r = Rational('Hello')
except ValueError as e:
    print(e)
try:
    r = Rational('1 / deux')
except ValueError as e:
    print(e)
