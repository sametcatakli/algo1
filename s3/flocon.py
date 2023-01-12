import turtle

jean = turtle.Turtle()
jean.speed(0)


def wait():
    input("press a key to stop")


def koch(t, x, seuil):
    if x < seuil:
        t.forward(x)

    else:
        koch(t, x / 3, seuil)
        t.left(60)
        koch(t, x / 3, seuil)
        t.left(-120)
        koch(t, x / 3, seuil)
        t.left(60)
        koch(t, x / 3, seuil)


def flocon(t, x, seuil):
    for i in range(3):
        koch(t, x, seuil)
        t.right(120)


flocon(jean, 350, 3)
wait()