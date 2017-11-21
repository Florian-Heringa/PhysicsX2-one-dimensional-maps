import math
import numpy as np
import matplotlib.pyplot as plt

from maps import *

class cobweb():

    def __init__(self, map):
        self.map = map

    def draw_cobweb(self, n, r, x0):

        f, ax = plt.subplots()
        ax.set_title("Cobweb for %s with n = %d" % (self.map, n))
        ax.set_xlabel("$x_n$")
        ax.set_ylabel("$x_{n+1}$")
        ## Plot the function
        x_list = [x for x in np.arange(0, 1, 0.01)]
        ax.plot(x_list, [self.map.f(x, r) for x in x_list], 'r-')
        ## Plot the line y = x
        ax.plot(x_list, x_list, 'k-')

        ## Set up initial values
        x_p, y_p = (x0, 0)
        x_i, y_i = (0, 0)

        for i in range(n):

            x_i, y_i = (x_p, self.map.f(x_p, r))

            ax.plot([x_p, x_i], [y_p, y_i], 'b-')
            ax.plot([x_i, y_i], [y_i, y_i], 'b-')

            x_p, y_p = (y_i, y_i)

        
        plt.show()