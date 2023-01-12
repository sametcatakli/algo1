"""Pour executer ce script, vous devez installer matplotlib"""
from random import *

import matplotlib.pyplot as plt
import itertools

import sort
import umons_cpu


class CpuPlot(object):
    def __init__(self, n):
        """
        Initialize an object that will be used to display data points on the
        screen.
        n   --  An array of x-values.
        """

        self.n = n
        self.courbes = []
        self.labels = []

    def prepare(self, data, label=None):
        """
        Add a data points.
        """

        self.courbes.append(data)
        self.labels.append(label)

    def reset(self):
        """
        Reset data points. Note that x-values are keeped.
        """

        self.courbes = []

    def draw(self):
        """
        Draw the data points on the screen.
        """

        plt.xlim(max(0, min(self.n) - 5), max(self.n) + 5)
        plt.ylim(0, max([max(t) for t in self.courbes]) + 5)

        plt.xlabel('input size')
        plt.ylabel('milliseconds')
        plt.title('CPU time charts')

        color = itertools.cycle('bgrcmyk')

        for i, t in enumerate(self.courbes):
            if self.labels[i] is None:
                plt.plot(self.n, t, '%s-o' % next(color),
                         label='Data points %d' % i)
            else:
                plt.plot(self.n, t, '%s-o' % next(color),
                         label=self.labels[i])

        plt.legend()
        plt.show()


if __name__ == '__main__':

    t1 = list(range(10))
    t2 = list(range(10, 0, -1))
    t3 = []
    for i in range(10):
        t3.append(randint(0, 10))
    # Create a CpuPlot object for x-values 10, 20, 30, 40
    afficheur = CpuPlot([0, 100, 200, 300, 400, 500, 600, 700, 800, 900])
    # Add two sets of data points

    for i in range(100):
        one = umons_cpu.cpu_time(sort.selection_sort, t1)

    for i in range(200):
        two = umons_cpu.cpu_time(sort.selection_sort, t1)

    for i in range(300):
        three = umons_cpu.cpu_time(sort.selection_sort, t1)

    for i in range(400):
        four = umons_cpu.cpu_time(sort.selection_sort, t1)

    for i in range(500):
        five = umons_cpu.cpu_time(sort.selection_sort, t1)

    for i in range(600):
        six = umons_cpu.cpu_time(sort.selection_sort, t1)

    for i in range(700):
        seven = umons_cpu.cpu_time(sort.selection_sort, t1)

    for i in range(800):
        eight = umons_cpu.cpu_time(sort.selection_sort, t1)

    for i in range(900):
        nine = umons_cpu.cpu_time(sort.selection_sort, t1)

    afficheur.prepare([0, one, two, three, four, five, six, seven, eight, nine], "Points 1")
    print(one, two, three, four, five, six, seven, eight, nine)
    # Display
    afficheur.draw()

    # Don't exit too fast
    input("Press [Enter] to exit.")
