""" Devrait afficher dans la console:
1/3 + 2/5 = 11/15
0.333333333333 + 0.4 = 0.733333333333
"""

""" Methode a definir:
    __float__(self)
"""

from rational import Rational

p = Rational(1, 3)
q = Rational(2, 5)

print(p, '+', q, '=', p + q)
print(float(p), '+', float(q), '=', float(p + q))

