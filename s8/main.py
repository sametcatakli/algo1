from sort import *
from umons_cpu import *
from random import *
from displayCpu import *

t1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
t2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
t3 = [2, 5, 9, 7, 1, 8, 4, 6, 3, 12, 11, 13, 10, 15, 16, 14, 17, 19, 18, 20]


def tri_bulle(t):
    i = 1
    while i != 0:
        i = 0
        for j in range(len(t) - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                i += 1


test = [2, 1, 4, 6, 3, 27, 5, 56, 43]

a1t1 = cpu_time(insertion_sort, t1)
a1t2 = cpu_time(insertion_sort, t2)
a1t3 = cpu_time(insertion_sort, t3)

a2t1 = cpu_time(selection_sort, t1)
a2t2 = cpu_time(selection_sort, t2)
a2t3 = cpu_time(selection_sort, t3)

a3t1 = cpu_time(merge_sort, t1)
a3t2 = cpu_time(merge_sort, t2)
a3t3 = cpu_time(merge_sort, t3)

print(a1t1)
print(a1t2)
print(a1t3)

print(a2t1)
print(a2t2)
print(a2t3)

print(a3t1)
print(a3t2)
print(a3t3)

afficheur1 = CpuPlot([1, 2, 3])

# Add two sets of data points
afficheur1.prepare([a1t1, a1t2, a1t3], "insertion")
afficheur1.prepare([a2t1, a2t2, a2t3], "selection")
afficheur1.prepare([a3t1, a3t2, a3t3], "merge")

# Display
afficheur1.draw()

# Don't exit too fast
input("Press [Enter] to exit.")