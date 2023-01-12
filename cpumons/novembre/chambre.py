def trouver(chambre, etiquette):
    objets = []
    position = []
    for i in chambre:
        for j in i:
            if j not in objets:
                objets.append(j)
                
    if etiquette not in objets:
        return []

    for i in range(len(chambre)):
        for j in range(len(chambre[i])):
            if chambre[i][j] == etiquette:
                position.append((i, j))
    return position


chambre = [["A", "A", "B", "D"], ["C", "P", "U", "A"], ["M", "O", "N", "S"],
           ["A", "B", "D", "A"]]
print(trouver(chambre, "A"))
