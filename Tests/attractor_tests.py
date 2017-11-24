import sys
sys.path.append('..')

from attractor_system import *
from strange_attractor_3d import *

a, b, c = (0, 0, 0)

rossler_a = Attractor3D(Rossler, a, b, c)
rossler_a.set_params(0.2, 0.2, 4)
print(rossler_a.params)
rossler_a.plot(100000, 0.001, ax1 = 'X', ax2 = 'Y', x0=1, y0=1, z0=1)
rossler_a.plot3D(100000, 0.001, x0=1, y0=1, z0=1)

lorenz_a = Attractor3D(Lorenz, a, b, c)
lorenz_a.set_params(10, 28, 2.667)
lorenz_a.plot(10000, 0.001, x0=1, y0=1, z0=1)
lorenz_a.plot3D(10000, 0.001, x0=.01, y0=.01, z0=.1)