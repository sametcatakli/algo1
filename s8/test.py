"""
Ce script illustre comment utiliser le module umons_cpu

Auteur: Pierre Hauweele et Hadrien Mélot (Université de Mons), 2016
"""

from umons_cpu import cpu_time, calibrate
from math import sqrt


def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


def insertion_sort(t):
    n = len(t)
    for i in range(1, n):
        clef = t[i]
        j = i - 1
        while j >= 0 and t[j] > clef:
            t[j + 1] = t[j]
            j = j - 1
        t[j + 1] = clef


def selection_sort(t):
    n = len(t)
    for i in range(n - 1):
        small = i
        for j in range(i + 1, n):
            if t[j] < t[small]:
                small = j
        (t[i], t[small]) = (t[small], t[i])


t = cpu_time(fib_iter, 30)
print('Fibo(30), version itérative : %.6f ms' % t)
t = cpu_time(fib_rec, 30)
print('Fibo(30), version récursive : %.6f ms' % t)
print('')

l = list(range(1000))
t = cpu_time(selection_sort, l)
print('selection_sort(t) avec liste triée de 1000 entiers : %.6f ms' % t)
l = list(range(1000))
t = cpu_time(insertion_sort, l)
print('insertion_sort(t) avec liste triée de 1000 entiers : %.6f ms' % t)
print('')

t = cpu_time(sqrt, 1000000)
print('Calcul de sqrt(1000000)   : %.6f ms' % t)
t = cpu_time(str.upper, 'hello')
print('Calcul de \'hello\'.upper : %.6f ms' % t)
print('')

print('cpu_time adapte automatiquement le nombre de tests:')
n = calibrate(fib_iter, 30)
print('Fibo(30), version itérative : 3 séries de %d tests' % n)
n = calibrate(fib_rec, 30)
print('Fibo(30), version récursive : 3 séries de %d tests' % n)
print('\ncpu_time retourne le temps moyen (pour un test) de la plus rapide des séries.')
print('')
