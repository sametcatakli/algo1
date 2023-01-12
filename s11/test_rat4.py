""" Devrait afficher dans la console:
-1/4
-1/4
-3
2
0
1
"""

"""
Vous devez creer une methode get_denominator() qui retourne le denominateur
(et par coherence vous pourriez le faire egalement pour le numerateur)
Ce genre de methode est appellee un accesseur.
"""

from rational import Rational

print(Rational(-1, 4))
print(Rational(1, -4))
print(Rational(21, -7))
print(Rational(2))
print(Rational())
print(Rational(1,-1).get_denominator())
