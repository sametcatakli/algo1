km = 10
m = 43
s = 30


def course(km, m, s):
    miles = km * 0.621

    vitesse_s = miles / ((m * 60) + s)
    vitesse_h = vitesse_s * 3600

    temps_s = ((m * 60) + s) / miles

    print('Vitesse moyenne: ', vitesse_h, 'miles/h')
    print('Temps par miles: ', temps_s, 'sec/miles')


course(km, m, s)
