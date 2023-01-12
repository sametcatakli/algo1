def change(price, e1, e2, e3, e4, e5, ):
    money = (20 * e1) + (10 * e2) + (5 * e3) + (2 * e4) + (1 * e5)
    rendre = money - price
    rendre_p = money - price
    r1 = 20
    r2 = 10
    r3 = 5
    r4 = 2
    r5 = 1
    rx1 = 0
    rx2 = 0
    rx3 = 0
    rx4 = 0
    rx5 = 0
    if price == money:
        print('Rien à rendre')
        return
    elif price > money:
        print('Montant donné inférieur au prix')
        return
    elif price < money:
        if rendre >= r1:
            rendre = rendre - r1
            rx1 = rx1 + 1
            if rendre >= r2:
                rendre = rendre - r2
                rx2 = rx2 + 1
            if rendre >= r3:
                rendre = rendre - r3
                rx3 = rx3 + 1
            if rendre >= r4:
                rendre = rendre - r4
                rx4 = rx4 + 1
            if rendre >= r5:
                rendre = rendre - r5
                rx5 = rx5 + 1
        elif rendre >= r2:
            rendre = rendre - r2
            rx2 = rx2 + 1
            if rendre >= r3:
                rendre = rendre - r3
                rx3 = rx3 + 1
            if rendre >= r4:
                rendre = rendre - r4
                rx4 = rx4 + 1
            if rendre >= r5:
                rendre = rendre - r5
                rx5 = rx5 + 1
        elif rendre >= r3:
            rendre = rendre - r3
            rx3 = rx3 + 1
            if rendre >= r4:
                rendre = rendre - r4
                rx4 = rx4 + 1
            if rendre >= r5:
                rendre = rendre - r5
                rx5 = rx5 + 1
        elif rendre >= r4:
            rendre = rendre - r4
            rx4 = rx4 + 1
            if rendre >= r5:
                rendre = rendre - r5
                rx5 = rx5 + 1
        elif rendre >= r5:
            rendre = rendre - r5
            rx5 = rx5 + 1
    print("A rendre: ", rendre_p, "€,", rx1, rx2, rx3, rx4, rx5)
change(37, 2, 0, 0, 0, 0)
