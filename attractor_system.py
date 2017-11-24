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


################### -- Example systems
######### Rossler
def x_D(x, y, z, a, b, c):
    return -y - z
def y_D(x, y, z, a, b, c):
    return x + a * y
def z_D(x, y, z, a, b, c):
    return b + z * (x - c)

Rossler = System3D(x_D, y_D, z_D, "Rossler")

######### Lorenz
def lorenz_x(x, y, z, a, b, c):
    return a*(y - x)
def lorenz_y(x, y, z, a, b, c):
    return b*x - y - x*z
def lorenz_z(x, y, z, a, b, c):
    return x*y - c*z

Lorenz = System3D(lorenz_x, lorenz_y, lorenz_z, "Lorenz")