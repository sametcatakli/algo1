def convert(fichier):
    dico = {}
    with open(fichier) as file:
        for line in file:
            (key, value) = line.split()
            dico[key] = value
    return dico
