"""
Voir commentaires concernant ce module dans l'enonce de la serie de TP.
"""

import random
import umons_cpu


def python_sort(t):
    t.sort()


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


# permet d'avoir une interface in place, similaire aux autres tris
def merge_sort(t):
    t[:] = merge_sort_functionnal(t)


def merge_sort_functionnal(t):
    n = len(t)
    if n > 1:
        (t1, t2) = split(t)
        t1 = merge_sort_functionnal(t1)
        t2 = merge_sort_functionnal(t2)
        return merge(t1, t2)
    else:
        return t


def split(t):
    """ precondition: len(t) >= 2 """
    mid = len(t) // 2
    t1 = t[:mid]
    t2 = t[mid:]
    return (t1, t2)


def merge(t1, t2):
    if len(t1) == 0:
        return t2
    elif len(t2) == 0:
        return t1
    elif t1[0] < t2[0]:
        return [t1[0]] + merge(t1[1:], t2)
    else:
        return [t2[0]] + merge(t1, t2[1:])


def dicho_search(t, x):
    start = 0
    end = len(t) - 1
    mid = start + (end - start) // 2
    while (end - start > 0) and x != t[mid]:
        if x < t[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = start + (end - start) // 2
    if len(t) > 0 and x == t[mid]:
        return mid
    else:
        return None


def test(n):
    t1 = list(range(n))
    t2 = list(range(n, 0, -1))
    t3 = []
    for i in range(n):
        t3.append(random.randint(0, n))
    print('%7d %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f' % (
        n,
        umons_cpu.cpu_time(selection_sort, t1),
        umons_cpu.cpu_time(insertion_sort, t1),
        umons_cpu.cpu_time(merge_sort, t1),
        umons_cpu.cpu_time(selection_sort, t2),
        umons_cpu.cpu_time(insertion_sort, t2),
        umons_cpu.cpu_time(merge_sort, t2),
        umons_cpu.cpu_time(selection_sort, t3),
        umons_cpu.cpu_time(insertion_sort, t3),
        umons_cpu.cpu_time(merge_sort, t3)))


if __name__ == '__main__':
    print('Temps affiches en msec')
    print('      n '
          't1: sel '
          '    ins '
          '    mer '
          't2: sel '
          '    ins '
          '    mer '
          't3: sel '
          '    ins '
          '    mer')
    for i in range(100, 901, 100):
        test(i)
