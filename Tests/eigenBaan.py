import sys
sys.path.append('..')

from attractor_system import *
from strange_attractor_3d import *

import numpy as np
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#collection of datavectors
Xs = []
#initial parameter values
sigma, beta = [10, 8/3.0]
#initial position
x0, y0, z0 = [1, 1, 1]
# iteration parameter
N = 1000
dt = .01
dRho = .01
rho_0 = 0
rho_max = 2

#list of values for rho to evaluate
rhos = [2 + x for x in np.arange(rho_0, rho_max, dRho)]
ts = [n * dt for n in np.arange(0, N + 1)]

# create system from predefined functions in attractor_system
lorenz_attractor = Attractor3D(Lorenz, sigma, beta, 1)

# iterate over rhos
for rho in rhos:
    lorenz_attractor.set_param(2, rho)
    Xs.append(lorenz_attractor.iterate(N, dt, x0, y0, z0))

# Convert to np array (easier data handling in np) and extract data vectors for axes
data = np.array(Xs)
Xs = data[:,0]
Ys = data[:,1]
Zs = data[:,2]

# Get svd for every data vector
uX, sX, vX = np.linalg.svd(Xs)
uY, sY, vY = np.linalg.svd(Ys)
uZ, sZ, vZ = np.linalg.svd(Zs)


fig, ax = plt.subplots(1, 3)
ax[0].plot(ts, Xs[0], color="black")
ax[0].plot(ts, vX[0], color="red")

ax[1].plot(ts, Ys[0], color="black")
ax[1].plot(ts, vY[0], color="red")

ax[2].plot(ts, Zs[0], color="black")
ax[2].plot(ts, vZ[0], color="red")

plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(Xs[0], Ys[0], Zs[0], color="blue")
ax.plot(vX[0], vY[0], vZ[0], color="black", lw=0.5, label="SV = %s, %s, %s" % (sX[0], sY[0], sZ[0]))
ax.plot(vX[1], vY[1], vZ[1], color="red", lw=0.5, label="SV = %s, %s, %s" % (sX[1], sY[1], sZ[1]))
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor PCA")
ax.legend()

plt.show()