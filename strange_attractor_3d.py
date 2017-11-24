from attractor_system import *

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Attractor3D():

    def __init__(self, system, a, b, c):
        self.system = system
        self.params = (a, b, c)
        self.allowedaxes = ['X', 'Y', 'Z']

    def set_param(self, i, val):
        self.params = (val, b, c) if val == 0 else (a, val, c) if val == 1 else (a, b, val)

    def set_params(self, a, b, c):
        self.params = (a, b, c)

    def derivs(self, x, y, z):

        a, b, c = self.params

        x_d = self.system.fx(x, y, z, a, b, c)
        y_d = self.system.fy(x, y, z, a, b, c)
        z_d = self.system.fz(x, y, z, a, b, c)

        return x_d, y_d, z_d

    def iterate(self, N, dt, x0=0, y0=0, z0=0):

        xs, ys, zs = ([x0], [y0], [z0])

        for n in range(N):
            x_d, y_d, z_d = self.derivs(xs[-1], ys[-1], zs[-1])
            xs.append(xs[-1] + (x_d * dt))
            ys.append(ys[-1] + (y_d * dt))
            zs.append(zs[-1] + (z_d * dt))

        return xs, ys, zs

    def select_axis(self, ax):

        if ax == 'X':
            return 0
        elif ax == 'Y':
            return 1
        elif ax == 'Z':
            return 2

    def plot(self, N, dt, ax1 = 'X', ax2 = 'Y', x0=0, y0=0, z0=0):

        if ax1 not in self.allowedaxes or ax2 not in self.allowedaxes:
            print("Axes must be X, Y or Z")

        axes = self.iterate(N, dt, x0=x0, y0=y0, z0=z0)

        fig, ax = plt.subplots()

        ax.plot(axes[self.select_axis(ax1)], axes[self.select_axis(ax2)])
        ax.set_xlabel("%s Axis" % ax1)
        ax.set_ylabel("%s Axis" % ax2)
        ax.set_title("%s Attractor" % self.system)
        plt.show()

    def plot3D(self, N, dt, x0=0, y0=0, z0=0):

        xs, ys, zs = self.iterate(N, dt, x0=x0, y0=y0, z0=z0)

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        ax.plot(xs, ys, zs, lw=0.5)
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_zlabel("Z Axis")
        ax.set_title("%s Attractor" % self.system)

        plt.show()