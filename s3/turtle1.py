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


koch(jean, 200, 5)
wait()