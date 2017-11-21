import math
import matplotlib.pyplot as plt
import numpy as np
from maps import *

class orbit_diagram():

    # Initialisation, sets up default amount of point to use and takes in a
    # map object (as defined in map.py)
    def __init__(self, map):
        self.map = map
        self.set_points(300, 100)

    # Set amount of points to use before starting the plot (to let initial transients die out)
    # And set amount of points to plot per value of r
    def set_points(self, cutoff, points_used):
        self.cutoff = cutoff
        self.points_used = points_used
        self.total_iterations = cutoff + points_used

    # Select an initial x0 and select the range to plot (this defaults to the range of the map object if left blank)
    # Then for all desired values of r the corresponding values of x are calculated and stored in a list.
    # Finally they are plotted for every value of r.
    def orbit_diagram(self, x0, rmin=None, rmax=None, dr=None):

        if rmin==None:
            rmin=self.map.rmin
        if rmax==None:
            rmax=self.map.rmax
        if dr==None:
            dr=self.map.dr

        f, ax = plt.subplots()
        ax.set_title("Orbit diagram for %s" % self.map)

        for r in np.arange(rmin, rmax, dr):

            # Reset value of x and empty list
            xn = self.map.f(x0, r)
            rs = []
            xns = []

            for v in range(0, self.total_iterations):

                # Only add to list after initial transients
                if v > self.cutoff:
                    rs.append(r)
                    xns.append(xn)
                    
                # Calculate next value of x
                xn = self.map.f(xn, r)

            # Plot for curent value of r
            ax.plot(rs, xns, 'k,')

        ax.set_xlabel("Parameter (r)")
        ax.set_ylabel("Values of x")
        plt.show()