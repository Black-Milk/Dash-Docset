from numpy import linspace,exp
from numpy.random import randn
from scipy.interpolate import LSQUnivariateSpline
import matplotlib.pyplot as plt
x = linspace(-3,3,100)
y = exp(-x**2) + randn(100)/10
t = [-1,0,1]
s = LSQUnivariateSpline(x,y,t)
xs = linspace(-3,3,1000)
ys = s(xs)
plt.plot(x, y, '.-')
plt.plot(xs, ys)
plt.show()

# xs,ys is now a smoothed, super-sampled version of the noisy gaussian x,y
# with knots [-3,-1,0,1,3]
