from scipy import *
from scipy.special import jn, jn_zeros
def drumhead_height(n, k, distance, angle, t):
   nth_zero = jn_zeros(n, k)
   return cos(t)*cos(n*angle)*jn(n, distance*nth_zero)
theta = r_[0:2*pi:50j]
radius = r_[0:1:50j]
x = array([r*cos(theta) for r in radius])
y = array([r*sin(theta) for r in radius])
z = array([drumhead_height(1, 1, r, theta, 0.5) for r in radius])

import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = pylab.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.jet)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
pylab.show()
