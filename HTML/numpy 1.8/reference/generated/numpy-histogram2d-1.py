import matplotlib as mpl
import matplotlib.pyplot as plt

# Construct a 2D-histogram with variable bin width. First define the bin
# edges:

xedges = [0, 1, 1.5, 3, 5]
yedges = [0, 2, 3, 4, 6]

# Next we create a histogram H with random bin content:

x = np.random.normal(3, 1, 100)
y = np.random.normal(1, 1, 100)
H, xedges, yedges = np.histogram2d(y, x, bins=(xedges, yedges))

# Or we fill the histogram H with a determined bin content:

H = np.ones((4, 4)).cumsum().reshape(4, 4)
print H[::-1]  # This shows the bin content in the order as plotted
# [[ 13.  14.  15.  16.]
# [  9.  10.  11.  12.]
# [  5.   6.   7.   8.]
# [  1.   2.   3.   4.]]

# Imshow can only do an equidistant representation of bins:

fig = plt.figure(figsize=(7, 3))
ax = fig.add_subplot(131)
ax.set_title('imshow:
# equidistant')
im = plt.imshow(H, interpolation='nearest', origin='low',
# extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])

# pcolormesh can displaying exact bin edges:

ax = fig.add_subplot(132)
ax.set_title('pcolormesh:
# exact bin edges')
X, Y = np.meshgrid(xedges, yedges)
ax.pcolormesh(X, Y, H)
ax.set_aspect('equal')

# NonUniformImage displays exact bin edges with interpolation:

ax = fig.add_subplot(133)
ax.set_title('NonUniformImage:
# interpolated')
im = mpl.image.NonUniformImage(ax, interpolation='bilinear')
xcenters = xedges[:-1] + 0.5 * (xedges[1:] - xedges[:-1])
ycenters = yedges[:-1] + 0.5 * (yedges[1:] - yedges[:-1])
im.set_data(xcenters, ycenters, H)
ax.images.append(im)
ax.set_xlim(xedges[0], xedges[-1])
ax.set_ylim(yedges[0], yedges[-1])
ax.set_aspect('equal')
plt.show()
