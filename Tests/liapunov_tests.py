import sys
sys.path.append('..')

from maps import *
from liapunov import *

## Creation of maps
population = map(population_map, population_map_deriv, "Population map", 0, 4)
tent = map(tent_map, tent_map_deriv, "Tent map", 0, 2)

## Creation of liapunov object
liapunov_pop = liapunov(population)
liapunov_tent = liapunov(tent)
print(liapunov_pop)
print(liapunov_tent)

## Calculate exponent
l_t = liapunov_tent.calc_liapunov_exponent(1000, 0.01, .67)
print(l_t)
l_p = liapunov_pop.calc_liapunov_exponent(1000, .67, .67)
print(l_p)

## Generate plot
liapunov_tent.gen_liapunov_plot(1000, 0.01, .67)
liapunov_pop.gen_liapunov_plot(1000, 0.01, .67)