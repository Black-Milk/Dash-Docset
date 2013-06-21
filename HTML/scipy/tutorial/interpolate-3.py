import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Cubic-spline

x = np.arange(0,2*np.pi+np.pi/4,2*np.pi/8)
y = np.sin(x)
tck = interpolate.splrep(x,y,s=0)
xnew = np.arange(0,2*np.pi,np.pi/50)
ynew = interpolate.splev(xnew,tck,der=0)

plt.figure()
plt.plot(x,y,'x',xnew,ynew,xnew,np.sin(xnew),x,y,'b')
plt.legend(['Linear','Cubic Spline', 'True'])
plt.axis([-0.05,6.33,-1.05,1.05])
plt.title('Cubic-spline interpolation')
plt.show()

# Derivative of spline

yder = interpolate.splev(xnew,tck,der=1)
plt.figure()
plt.plot(xnew,yder,xnew,np.cos(xnew),'--')
plt.legend(['Cubic Spline', 'True'])
plt.axis([-0.05,6.33,-1.05,1.05])
plt.title('Derivative estimation from spline')
plt.show()

# Integral of spline

def integ(x,tck,constant=-1):
    x = np.atleast_1d(x)
    out = np.zeros(x.shape, dtype=x.dtype)
    for n in xrange(len(out)):
        out[n] = interpolate.splint(0,x[n],tck)
    out += constant
    return out
# >>>
yint = integ(xnew,tck)
plt.figure()
plt.plot(xnew,yint,xnew,-np.cos(xnew),'--')
plt.legend(['Cubic Spline', 'True'])
plt.axis([-0.05,6.33,-1.05,1.05])
plt.title('Integral estimation from spline')
plt.show()

# Roots of spline

print interpolate.sproot(tck)
# [ 0.      3.1416]

# Parametric spline

t = np.arange(0,1.1,.1)
x = np.sin(2*np.pi*t)
y = np.cos(2*np.pi*t)
tck,u = interpolate.splprep([x,y],s=0)
unew = np.arange(0,1.01,0.01)
out = interpolate.splev(unew,tck)
plt.figure()
plt.plot(x,y,'x',out[0],out[1],np.sin(2*np.pi*unew),np.cos(2*np.pi*unew),x,y,'b')
plt.legend(['Linear','Cubic Spline', 'True'])
plt.axis([-1.05,1.05,-1.05,1.05])
plt.title('Spline of parametrically-defined curve')
plt.show()
