def rec(nserie):
    res = 0
    for i in range(len(nserie)):
        res = res + nserie[i]
    if res > 99:
        resu = [int(x) for x in str(res)]
        rec(resu)
    else:
        print(res)
        return res


def winner(nserie):
    if rec(nserie) == 42:
        print('A une chance de gagner')
    else:
        print('N\'a pas de chance de gagner')


winner([1, 2, 3, 4, 9, 7, 1, 2, 3, 4, 6])
