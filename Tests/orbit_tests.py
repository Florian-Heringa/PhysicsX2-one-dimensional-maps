import math
import sys
sys.path.append('..')

from gen_orbit_diagram import *
from maps import *

## Creation of maps
population = map(population_map, population_map_deriv, "Logistic map", 0, 4)
# tent = map(tent_map, tent_map_deriv, "Tent map", 0, 2)
# sin = map(sin_map, sin_map_deriv, "Sine map", 0, math.pi)

## Orbit diagram of the tent map
# orb_tent = orbit_diagram(tent)
# orb_tent.set_points(100, 100)
# print(orb_tent)
# orb_tent.orbit_diagram(0.5, rmin = 2, rmax= 3, dr=0.001)

## Orbit diagram of the population map r * x * (1 - x)
orb_pop = orbit_diagram(population)
orb_pop.set_points(100, 200)
print(orb_pop)
orb_pop.orbit_diagram(0.5, rmin=2.8, rmax=4.0, dr=0.0005)

## Orbit diagram of sine map
# orb_sin = orbit_diagram(sin)
# orb_sin.set_points(100, 200)
# print(orb_sin)
# orb_sin.orbit_diagram(0.5, rmin=3.4/4, rmax=3.9/4, dr=0.0001)