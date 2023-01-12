""" Devrait afficher dans la console:
3/4 - Rational(3, 4)
300 - Rational(300, 1)
"""

from rational import Rational

r = Rational(0.75)
print(r, '-', repr(r))
r = Rational(300)
print(r, '-', repr(r))
