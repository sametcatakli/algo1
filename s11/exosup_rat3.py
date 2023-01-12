""" Devrait afficher dans la console:
False False False
True False True
"""

""" Methodes a definir:
    (verifiez bien les valeurs ci-dessus car Python affichera des valeurs
     booleennes - incorrectes - meme sans que les methodes suivantes soient definies !)

    __eq__(self, other) pour ==
    __lt__(self, other) pour <
    __le__(self, other) pour <=
"""

from rational import Rational

p = Rational(1, 3)
q = Rational(0.2)
r = Rational('2 / 10')

print(p == q, p < q, p <= q)
print(q == r, q < r, q <= r)

