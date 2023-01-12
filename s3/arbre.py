from uturtle import *

jean = umonsTurtle()


def wait():
    input('press a key to stop')


def arbre(t, x, a, n):
    if n != 0:
        moveForward(t, x)
        turnLeft(t, a)
        moveForward(t, x/2)
        arbre(t, x*2/3, a, n-1)
        moveBackward(t, x/2)
        turnRight(t, 2*a)
        moveForward(t, x/2)
        arbre(t, x*2/3, a, n-1)
        moveBackward(t, x/2)
        turnLeft(t, a)
        moveBackward(t, x)       
turnLeft(jean, 90)


arbre(jean, 50, 30, 5)


wait()
