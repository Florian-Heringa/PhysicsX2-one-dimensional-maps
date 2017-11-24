import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class System3D():

    def __init__(self, fx, fy, fz, name):
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Attractor3D():

    def __init__(self, system, a, b, c):
        self.system = system
        self.params = (a, b, c)
        self.allowedaxes = ['X', 'Y', 'Z']

    # def __init__(self, fx, fy, fz, a, b, c):
    #     self.system = System3D(fx, fy, fz)
    #     self.params = (a, b, c)
    #     self.allowedaxes = ['X', 'Y', 'Z']

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

def x_D(x, y, z, a, b, c):
    return -y - z
def y_D(x, y, z, a, b, c):
    return x + a * y
def z_D(x, y, z, a, b, c):
    return b + z * (x - c)

def lorenz_x(x, y, z, a, b, c):
    return a*(y - x)
def lorenz_y(x, y, z, a, b, c):
    return b*x - y - x*z
def lorenz_z(x, y, z, a, b, c):
    return x*y - c*z

a, b, c = (0, 0, 0)

Rossler = System3D(x_D, y_D, z_D, "Rossler")
rossler_a = Attractor3D(Rossler, a, b, c)
rossler_a.set_params(0.2, 0.2, 4)
print(rossler_a.params)
rossler_a.plot(100000, 0.001, ax1 = 'X', ax2 = 'Y', x0=1, y0=1, z0=1)
rossler_a.plot3D(100000, 0.001, x0=1, y0=1, z0=1)

Lorenz = System3D(lorenz_x, lorenz_y, lorenz_z, "Lorenz")
lorenz_a = Attractor3D(Lorenz, a, b, c)
lorenz_a.set_params(10, 28, 2.667)
lorenz_a.plot(10000, 0.001, x0=1, y0=1, z0=1)
lorenz_a.plot3D(10000, 0.001, x0=.01, y0=.01, z0=.1)