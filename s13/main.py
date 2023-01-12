def aire_polygone(liste):
    """Calcul l'aire d'un polygone à partir de sa liste de points via la récursivité"""
    if len(liste) == 3:
        return abs((liste[0][0] * liste[1][1] + liste[1][0] * liste[2][1] + liste[2][0] * liste[0][1] - \
                    liste[1][0] * liste[0][1] - liste[2][0] * liste[1][1] - liste[0][0] * liste[2][1]) / 2)
    else:
        return abs((liste[0][0] * liste[1][1] + liste[1][0] * liste[2][1] + liste[2][0] * liste[0][1] - \
                    liste[1][0] * liste[0][1] - liste[2][0] * liste[1][1] - liste[0][0] * liste[2][1]) / 2) + \
               aire_polygone(liste[1:] + [liste[0]])


               
print(aire_polygone([(0, 0), (1, 0), (1, 1), (0, 1)]))
    
