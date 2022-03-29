from lagrange import Lagrange
from newton import Newton
from generators import *

import matplotlib.pyplot as plt

# Draw interpolated function. User passes method of interpolation and point generation
def draw(interpolator: Newton | Lagrange, a: float, b: float, label="", samples=1000):
    xs = generate_intervals(samples, a, b)
    results = [0] * samples

    for i in range(samples):
        results[i] = interpolator.interpolate(xs[i])
    plt.plot(xs, results, label=label)
    return results


# Draw a single parameter function, at points generated by a chosen method (dists)
def draw_funct(func, a: float, b: float, samples=1000):
    points = generate_intervals(samples, a, b)
    results = [func(points[i]) for i in range(samples)]
    plt.plot(points, results, label="function")
    return results