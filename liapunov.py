import math
import sys
import numpy as np
import random as rd
import matplotlib.pyplot as plt

###########--Liapunov class--###################

class liapunov():

    def __init__(self, map):
        self.map = map

    def __repr__(self):
        return "Liapunov object with %s" % repr(self.map)

    def calc_liapunov_exponent(self, n, r, x0):
        """
        Liaponov exponent, n, r, x0
        """

        return self.deriv_sum(n, r, x0) / n

    def deriv_sum(self, n, r, x0):

        x_i = x0
        arg = 0

        for i in range(n):

            arg += math.log(abs(self.map.f_d(x_i, r)))
            x_i = self.map.f(x_i, r)

        return arg
    
    def gen_seperation_plot(self, N, r, dx):

        f, ax = plt.subplots()
        ax.set_title("Seperation plot for %s with r = %f" % (self.map, r))
        ax.set_xlabel("Iterations")
        ax.set_ylabel("x/dx")

        x1 = rd.random()
        x2 = x1 + dx

        x1s = [x1]
        x2s = [x2]
        dxs = [dx]
        ns = [0]

        for n in range(1, N + 1):
            ns.append(n)
            x1s.append(self.map.f(x1s[-1], r))
            x2s.append(self.map.f(x2s[-1], r))
            dxs.append(x1s[-1] - x2s[-1])

        ax.plot(ns, x1s, 'r-.', label="x1")
        ax.plot(ns, x2s, 'b--', label="x2")
        ax.plot(ns, dxs, 'k-', label="dx")
        ax.legend()
        plt.show()

    def gen_liapunov_plot(self, n, dr, x0):
        """
        Liaponov exponent plot: n, dr, x0
        """

        r_l = []
        l_l = []

        for r in np.arange(self.map.rmin + dr, self.map.rmax, dr):

            l = self.calc_liapunov_exponent(n, r, x0)

            r_l.append(r)
            l_l.append(l)

        plt.plot(r_l, l_l)
        plt.xlabel("r")
        plt.ylabel("Liapunov exponent ($\lambda$)")
        plt.title("%s" % self.map)
        plt.show()