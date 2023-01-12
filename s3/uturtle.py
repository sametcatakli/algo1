#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Module permettant de manipuler une tortue en mode procédural
    Utilisé dans le cadre du cours de Programmation et Algorithmique 1
    (H. Mélot, Université de Mons, à partir de 2013)
"""

import turtle

turtle.setup(500, 400)


def umonsTurtle():
    """ Retourne une tortue qui peut évoluer dans un écran
    (déjà initialisé).

    """
    t = turtle.Turtle()
    return t


def wait(msg='Press enter to quit.'):
    """ Affichage un message à l'écran et attend une interaction de
    l'utilisateur.

    msg - le message à afficher.

    """
    input(msg)


def moveForward(t, x):
    """ Fait avancer une tortue t de x pixels.

    t - une tortue
    x - nombre de pixels

    """
    t.fd(x)


def moveBackward(t, x):
    """ Fait reculer une tortue t de x pixels.

    t - une tortue
    x - nombre de pixels

    """
    t.bk(x)


def turnRight(t, a=90):
    """ Fait tourner une tortue t de a degrés vers la droite.

    t - une tortue
    a - angle en degrés
    """
    t.rt(a)


def turnLeft(t, a=90):
    """ Fait tourner une tortue t de a degrés vers la gauche.

    t - une tortue
    a - angle en degrés

    """
    t.lt(a)


def dropPen(t):
    """ Demande à une tortue t de soulever son stylo

    t - une tortue

    """
    t.up()


def usePen(t):
    """ Demande à une tortue t d'abaisser son stylo

    t - une tortue

    """
    t.down()


if __name__ == '__main__':
    bob = umonsTurtle()
    moveForward(bob, 100)
    turnRight(bob)
    moveForward(bob, 100)
    wait()
