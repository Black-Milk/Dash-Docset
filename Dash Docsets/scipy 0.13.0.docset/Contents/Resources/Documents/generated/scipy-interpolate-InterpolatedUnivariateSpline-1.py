from numpy import linspace,exp
from numpy.random import randn
from scipy.interpolate import InterpolatedUnivariateSpline
import matplotlib.pyplot as plt
x = linspace(-3, 3, 100)
y = exp(-x**2) + randn(100)/10
s = InterpolatedUnivariateSpline(x, y)
xs = linspace(-3, 3, 1000)
ys = s(xs)
plt.plot(x, y, '.-')
plt.plot(xs, ys)
plt.show()

# xs,ys is now a smoothed, super-sampled version of the noisy gaussian x,y
