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
        self.dr = (rmax-rmin)/1000.

    def __str__(self):
        return self.name

    def __repr__(self):
        return "%s: {rmin: %.2f, rmax: %.2f, dr: %.3f}" % (self.name, self.rmin, self.rmax, self.dr)

###########--Maps--#######################


################ Tent map
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

################# Population map

def population_map(xn, r):
    return r * xn * (1 - xn)

def population_map_deriv(xn, r):
    return r - 2 * r * xn

################ Sine map

def sin_map(xn, r):
    return r * math.sin(math.pi * xn)

def sin_map_deriv(xn, r):
    return r * math.pi * math.cos(math.pi * xn)

################ Cosine map
## Defined such that the entire function falls within the unit square
## [0, 1] x [0, 1]

def cos_map(xn, r):
    return (r * math.cos(math.pi * xn) + 1) / 2

def cos_map_deriv(xn, r):
    return (-r * math.pi * math.sin(math.pi * xn)) / 2