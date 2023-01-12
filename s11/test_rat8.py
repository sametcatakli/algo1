""" Devrait afficher dans la console:
11/15 -5/3 7/12 11/15 -5/3 7/12
2/15 -2/3 1/12 2/15 -2/3 1/12
"""

""" Methodes a definir:
    __add__(self, other), __radd__(self, other)
    __mul__(self, other), __rmul__(self, other)
"""

from rational import Rational

p = Rational(1, 3)
q = Rational(2, 5)
r = -2
s = 0.25

print(p + q, p + r, p + s, q + p, r + p, s + p)
print(p * q, p * r, p * s, q * p, r * p, s * p)
