import turtle

jean = turtle.Turtle()
jean.speed(0)


def koch(t, x, seuil):
    if seuil == 0:
        t.forward(x)
    else:
        koch(t, x / 3, seuil - 1)
        t.left(90)
        koch(t, x / 3, seuil - 1)
        t.right(90)
        koch(t, x / 3, seuil - 1)
        t.right(90)
        koch(t, x / 3, seuil - 1)
        t.left(90)
        koch(t, x / 3, seuil - 1)


def flocon(t, x, seuil):
    koch(t, x, seuil)
    t.right(180)


flocon(jean, 500, 5)

