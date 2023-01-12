def orni(n, m):
    ligne = ["" * n] * n
    champ = []
    for i in range(4):
        champ.append(ligne)
    print(champ)

    for k in range(len(m)):
        i = m[k][0]
        j = m[k][1]
        champ[i][j] = "O"
    print(champ)


orni(4, [(1, 2), (2, 1), (2, 2)])
