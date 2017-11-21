import math

###########--Map class--##############

class map():

    # Holds data for a map, its function and its derivative (used in liapunov exponent)
    # Also the value of the parameter for which the maps is defined is specified.
    def __init__(self, f, f_d, name, rmin, rmax):
        self.f = f
        self.f_d = f_d
        self.name = name
        self.rmin = rmin
        self.rmax = rmax
        self.dr = (rmax-rmin)/100.

    def __str__(self):
        return self.name

###########--Maps--#######################

def tent_map(x, r):

    if 0 <= x and x <= 0.5:
        return r * x
    elif 0.5 <= x and x <= 1:
        return r - r * x
    else:
        return 0

def tent_map_deriv(x, r):

    if 0 <= x and x <= 0.5:
        return r
    elif 0.5 <= x and x <= 1:
        return -r
    else:
        return 0

def population_map(xn, r):
    return r * xn * (1 - xn)

def population_map_deriv(xn, r):
    return r - 2 * r * xn