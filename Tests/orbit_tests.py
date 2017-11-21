import sys
sys.path.append('..')

from gen_orbit_diagram import *
from maps import *

## Creation of maps
population = map(population_map, population_map_deriv, "Population map", 0, 4)
tent = map(tent_map, tent_map_deriv, "Tent map", 0, 2)

## Orbit diagram of the tent map
orb_tent = orbit_diagram(tent)
orb_tent.set_points(100, 100)
print(orb_tent)
orb_tent.orbit_diagram(0.5, dr=0.001)

## Orbit diagram of the population map r * x * (1 - x)
orb_pop = orbit_diagram(population)
orb_pop.set_points(100, 200)
print(orb_pop)
orb_pop.orbit_diagram(0.5, rmin=3.4, rmax=3.9, dr=0.0005)