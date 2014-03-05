xp = [1, 2, 3]
fp = [3, 2, 0]
np.interp(2.5, xp, fp)
# 1.0
np.interp([0, 1, 1.5, 2.72, 3.14], xp, fp)
# array([ 3. ,  3. ,  2.5 ,  0.56,  0. ])
UNDEF = -99.0
np.interp(3.14, xp, fp, right=UNDEF)
# -99.0

# Plot an interpolant to the sine function:

x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)
xvals = np.linspace(0, 2*np.pi, 50)
yinterp = np.interp(xvals, x, y)
import matplotlib.pyplot as plt
plt.plot(x, y, 'o')
# [<matplotlib.lines.Line2D object at 0x...>]
plt.plot(xvals, yinterp, '-x')
# [<matplotlib.lines.Line2D object at 0x...>]
plt.show()
