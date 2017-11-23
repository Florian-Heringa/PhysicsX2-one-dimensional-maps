import math

# Find a stable point for the map func, starting at random point x0
# min_dx defines how close two successive points must be to classify as
# a fixed point
#
# Function returns a tuple with the value of the fixed point and the amount
# of iterations used to find it.
def find_stable(func, min_dx, x0, r = 0):

    xn = func(x0) if func.__code__.co_argcount == 1 else func(x0, r)
    xt = 0
    iterations = 0
    dx = abs(xn - x0)

    while dx > min_dx:

        xt = xn
        xn = func(xn) if func.__code__.co_argcount == 1 else func(xn, r)
        dx = abs(xt - xn)

        iterations += 1

        if dx > (func(xn) if func.__code__.co_argcount == 1 else func(xn, r)) * (1/min_dx) or iterations > 10000:
            return 'inf', iterations

    return xn, iterations

# xn+1 = xn**2
print(find_stable(lambda x : x * x, 0.00001, .7381298614))
# xn+1 = sin(xn)
print(find_stable(lambda x : math.sin(x), 0.00001, 1))
# xn+1 = cos(xn)
print(find_stable(lambda x : math.cos(x), 0.00001, 1))
# xn+1 = r xn (1 - xn)
print(find_stable(lambda x, r: r * x * (1 - x), 0.67, 1, r = 3))