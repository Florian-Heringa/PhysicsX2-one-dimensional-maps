from maps import *

class Feigenbaum():

    def __init__(self, map):

        self.map = map

    def calculate(self):

        

    def actual(self):

        maxIt = 13
        maxItJ = 10
        a_1 = 1.0
        a_2 = 0.0
        d_1 = 3.2
        print( 'i, d')
        for i in range(2, maxIt):
            a = a_1 + (a_1 - a_2) / d_1
            for j in range(maxItJ):
                x = 0
                y = 0
                for k in range(2 ** i):
                    y = 1 - 2 * y * x
                    x = a - x * x    
                a = a - x / y
            d = (a_1 - a_2) / (a - a_1)
            print("%02i %f" % (i, d))
            d_1 = d
            a_2 = a_1
            a_1 = a

population = map(population_map, population_map_deriv, "Population map", 0, 4)
f = Feigenbaum(population)
print(f.actual())
