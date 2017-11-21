import math
import sys
sys.path.append('..')

from cobweb import *
from maps import *

## Creation of maps
population = map(population_map, population_map_deriv, "Population map", 0, 4)
tent = map(tent_map, tent_map_deriv, "Tent map", 0, 2)
sin = map(sin_map, sin_map_deriv, "Sine map", 0, math.pi)
cos = map(cos_map, cos_map_deriv, "Cosine map", 0, math.pi)

## Test for population
cw_pop = cobweb(population)
cw_pop.draw_cobweb(100, .5, .51)

## Test for tent
cw_tent = cobweb(tent)
cw_tent.draw_cobweb(100, .5, .51)

## Test for sine
cw_sin = cobweb(sin)
cw_sin.draw_cobweb(100, .5, .51)

## Test for cosine
cw_cos = cobweb(cos)
cw_cos.draw_cobweb(1000, 1, .45)