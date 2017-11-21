import math

# Find a stable point for the map func, starting at random point x0
# min_dx defines how close two successive points must be to classify as
# a fixed point
#
# Function returns a tuple with the value of the fixed point and the amount
# of iterations used to find it.
def find_stable(func, min_dx, x0):

    xn = func(x0)
    xt = 0
    iterations = 0
    dx = abs(xn - x0)

    while dx > min_dx:

        xt = xn
        xn = func(xn)
        dx = abs(xt - xn)

        iterations += 1

        if dx > func(x0) * (1/min_dx) or iterations > 10000:
            return 'inf', iterations

    return xn, iterations

# xn+1 = xn**2
print(find_stable(lambda x : x * x, 0.00001, .7381298614))
# xn+1 = sin(xn)
print(find_stable(lambda x : math.sin(x), 0.00001, 1))
# xn+1 = cos(xn)
print(find_stable(lambda x : math.cos(x), 0.00001, 1))