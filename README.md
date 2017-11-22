# PhysicsX2-one-dimensional-maps

This repository stores multiple ways of analysing one-dimensional maps defined on the unit square.
All instances of x0 expect a random value of x0 in the range \[0, 1\]

## Map

This class stores the representation of a map, together with it's derivative (used for finding the liapunov exponent)
and the range of allowed valus of the parameter r.

## Cobweb

Draws a cobweb diagram for a map as given by the map class

## Liapunov

Calculates the liapunov exponent by iterating the map n times and determining theseperation from the initial position.

## gen_orbit_diagram

Make an orbit diagram for a given map. Optional arguments can be given to restrict the range and resolution of the r-axis to
speed up computation.

## find_stable

Find the value of a stable point (if any), if no point is found within an appreciable amount of iterations
the function returns \inf
