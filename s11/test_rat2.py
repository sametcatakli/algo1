""" Devrait afficher dans la console:
1/2
2/4
2/1
Cannot create 3/0: zero in denominator
"""

"""
ZeroDivisionError existe en Python: vous devez juste lancer
    cette exception sans devoir la creer.
"""
from rational import Rational

r = Rational(1, 2)
print(r)
r = Rational(2, 4)
print(r)
r = Rational(2, 1)
print(r)
try:
    r = Rational(3, 0)
except ZeroDivisionError as e:
    print(e)

