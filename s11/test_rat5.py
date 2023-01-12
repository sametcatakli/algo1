""" Devrait afficher dans la console:
Cannot create a rational with a numerator of <class 'float'>
Cannot create a rational with a denominator of <class 'float'>
Cannot create a rational with a numerator of <class 'str'>
Cannot create a rational with a denominator of <class 'str'>
Cannot create a rational with a numerator of <class 'list'>
Cannot create a rational with a denominator of <class 'list'>
Cannot create a rational with a numerator of <class 'bool'>
Cannot create a rational with a denominator of <class 'bool'>
1/2
"""

""" Note:
Cela devrait avoir le meme comportement pour tout type (hors int)

Pour pouvoir indiquer le type dans le msg d'erreur:
    str(type(x))
(car type ne retourne pas un str)
"""

from rational import Rational

try:
    r = Rational(1.0)
except ValueError as e:
    print(e)
try:
    r = Rational(1, 1.0)
except ValueError as e:
    print(e)
try:
    r = Rational('Hello')
except ValueError as e:
    print(e)
try:
    r = Rational(1, 'Hello')
except ValueError as e:
    print(e)
try:
    r = Rational([1, 2])
except ValueError as e:
    print(e)
try:
    r = Rational(1, [1, 2])
except ValueError as e:
    print(e)
try:
    r = Rational(True)
except ValueError as e:
    print(e)
try:
    r = Rational(1, True)
except ValueError as e:
    print(e)
try:
    r = Rational(1, 2)
    print(r)
except ValueError as e:
    print(e)

