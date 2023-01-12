""" Devrait afficher dans la console:
-1/15 7/3 1/12 1/15 -7/3 -1/12
5/6 -1/6 4/3 6/5 -6 3/4
"""

""" Methodes a definir:
    __sub__(self, other), __rsub__(self, other)
    __truediv__(self, other), __rmul__(self, other)
"""

from rational import Rational

p = Rational(1, 3)
q = Rational(2, 5)
r = -2
s = 0.25

print(p - q, p - r, p - s, q - p, r - p, s - p)
print(p / q, p / r, p / s, q / p, r / p, s / p)

