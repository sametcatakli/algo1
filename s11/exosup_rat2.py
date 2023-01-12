""" Devrait afficher dans la console:
num of p =  1
den of p =  2
Bad index for [] operator: use 2 but only 0 and 1 are accepted
1/6
1/2
Bad index for [] operator: use -1 but only 0 and 1 are accepted
Cannot set zero in denominator
"""

""" Methodes a definir:
    __getitem__(self, index) ou index = {0, 1}
    __setitem__(self, index, value) ou index = {0, 1}

    L'indice 0 represente le numerateur
    L'indice 1 represente le denominateur
"""

from rational import Rational

p = Rational(2, 4)
print("num of p = ", p[0])
print("den of p = ", p[1])
try:
    print(p[2])
except IndexError as e:
    print(e)

p[1] = 6
print(p)
p[0] = 3
print(p)
try:
    p[-1] = 2
    print(p)
except IndexError as e:
    print(e)
try:
    p[1] = 0
    print(p)
except ZeroDivisionError as e:
    print(e)
