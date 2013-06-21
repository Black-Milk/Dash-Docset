import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# InterpolatedUnivariateSpline

x = np.arange(0,2*np.pi+np.pi/4,2*np.pi/8)
y = np.sin(x)
s = interpolate.InterpolatedUnivariateSpline(x,y)
xnew = np.arange(0,2*np.pi,np.pi/50)
ynew = s(xnew)

plt.figure()
plt.plot(x,y,'x',xnew,ynew,xnew,np.sin(xnew),x,y,'b')
plt.legend(['Linear','InterpolatedUnivariateSpline', 'True'])
plt.axis([-0.05,6.33,-1.05,1.05])
plt.title('InterpolatedUnivariateSpline')
plt.show()

# LSQUnivarateSpline with non-uniform knots

t = [np.pi/2-.1,np.pi/2+.1,3*np.pi/2-.1,3*np.pi/2+.1]
s = interpolate.LSQUnivariateSpline(x,y,t,k=2)
ynew = s(xnew)

plt.figure()
plt.plot(x,y,'x',xnew,ynew,xnew,np.sin(xnew),x,y,'b')
plt.legend(['Linear','LSQUnivariateSpline', 'True'])
plt.axis([-0.05,6.33,-1.05,1.05])
plt.title('Spline with Specified Interior Knots')
plt.show()
