from math import sqrt

def droite(p1, p2):
    x1 = float(p1[0])
    y1 = float(p1[1])
    x2 = float(p2[0])
    y2 = float(p2[1])

    # print(x1, x2, y1, y2)

    deno = (x2 - x1)
    nume = (y2 - y1)
    if nume == 0:
        return None
    elif deno == 0:
        return "(1, 0, 0)"
    else:
        pente = nume / deno
        ordonnee = y2 - pente * x2
        y = ordonnee
        return - pente, y, + ordonnee


def appartient(d, p):
    a = float(d[0])
    b = float(d[1])
    c = float(d[2])

    x1 = float(p[0])
    y1 = float(p[1])

    if (a * x1) + (b * y1) == c:
        return True
    else:
        return False

    return a, b, c, x1, y1


def paralleles(d1, d2):
    a1 = float(d1[0])
    a2 = float(d2[0])
    pente1 = - a1
    pente2 = - a2

    if pente1 == pente2:
        return True
    else:
        return False


def intersection(d1, d2):
    a1 = float(d1[0])
    b1 = float(d1[1])
    c1 = float(d1[2])

    a2 = float(d2[0])
    b2 = float(d1[1])
    c2 = float(d1[2])

    pente1 = - a1
    pente2 = - a2

    if pente1 == pente2:
        return None
    else:
       
       x = -b1 - c1 / a1

       y = -(a1) + (c1)

       return x, y



def droite_normale(d, p): 
    a1 = float(d[0])
    b1 = float(d[1])
    c1 = float(d[2])

    p1 = float(p[0])
    p2 = float(p[1])

    x = p1
    y = p2

    d = a1 * x + b1 * y - c1
    
    a2 = 1 / -a1
    b2 = b1
    c2 = (a2 * x) + (b2 * y)
    
    return(a2 ,b2, c2)


def symetrie_orthogonale(d, p):
    a = float(d[0])
    b = float(d[1])
    c = float(d[2])

    x = p[0]
    y = p[1]

    num = a * x + b * y + (-c) 
    deno = sqrt( (a**2) + (b**2) )
    distance = num / deno

    """ 
    la droite donné est le milieu du segment entre le point et sa symétrie,
    il faut tracer la droite perpendiculaire à d passant par le point donné et
    aller dans l'autre sens à partir de l'intersection jusqu'au point qui
    se situe à la même distance que le point donné par rapport à d.

    Comment faire ça en python ?

    pas trouvé
    """

    return 'pas trouvé'
    
    
    
def distance_droite_point(d, p):
    a = float(d[0])
    b = float(d[1])
    c = float(d[2])

    x = p[0]
    y = p[1]

    num = a * x + b * y + (-c) 
    deno = sqrt( (a**2) + (b**2) )
    distance = num / deno
    return distance