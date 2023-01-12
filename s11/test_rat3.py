""" Devrait afficher dans la console:
1/2
1/2
2
Cannot create 3/0: zero in denominator
"""

"""
Dorenavant, vos rationnels doivent se simplifier automatiquement !
"""

from rational import Rational

print(Rational(1, 2))
print(Rational(2, 4))
print(Rational(2, 1))
print(Rational(26, 13))
try:
    print(Rational(3, 0))
except ZeroDivisionError as e:
    print(e)

