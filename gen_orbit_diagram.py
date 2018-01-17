import math
import matplotlib.pyplot as plt
import numpy as np
from maps import *
import statistics

class orbit_diagram():

    # Initialisation, sets up default amount of point to use and takes in a
    # map object (as defined in map.py)
    def __init__(self, map):
        self.map = map
        self.set_points(300, 100)

    def __repr__(self):
        return "Orbit diagram object with %s. Points {cutoff: %d, used %d}" % (repr(self.map), self.cutoff, self.points_used)

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

        # parameters for finding n-cycles
        reset = True
        nprev = 0
        rprev = rmin
        cycles = []
        ns = []

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
            
            # detect n-cycles up to 6
            try:
                hist = np.histogram(xns, bins = 100)
                n = len(find_peaks(hist[0], 25, 0.8))
                if n <= 6 and n > 0 and nprev != n and n > 1 and r - rprev > 0.1:
                    print(r)
                    ax.plot([r, r], [0, 1])
                    cycles.append(n)
                    rprev = r
            except ValueError as e:
                print(e)

            nprev = n
            ns.append(n/10.0)

            # Plot for curent value of r
            ax.plot(rs, xns, 'k,')
        ax.plot([r for r in np.arange(rmin, rmax, dr)], ns)
        print(cycles)
        for i in range(len(cycles)-1):
            try:
                while cycles[i] == cycles[i+1]:
                    del cycles[i+1]
            except IndexError as e:
                print(e)
                break
        print(cycles)


        ax.set_xlabel("Parameter; r")
        ax.set_ylabel("Allowed values of x")
        ax.set_xlim([rmin, rmax])
        ax.set_ylim(0)
        plt.show()


def find_peaks(a, d, s):
  x = np.array(a)
  max = np.max(x)
  length = len(a)
  ret = []
  for i in range(length):
      ispeak = True
      if i-1 > 0:
          ispeak &= (x[i] > d * x[i-1])
      if i+1 < length:
          ispeak &= (x[i] > d * x[i+1])

      ispeak &= (x[i] > s * max)
      if ispeak:
          ret.append(i)
  return ret