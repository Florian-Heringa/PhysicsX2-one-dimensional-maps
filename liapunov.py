import math
import sys
import numpy as np
import matplotlib.pyplot as plt

###########--Liapunov class--###################

class liapunov():

    def __init__(self, map):
        self.map = map

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