# Triangulation of a set of points:

points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
from scipy.spatial import Delaunay
tri = Delaunay(points)

# We can plot it:

import matplotlib.pyplot as plt
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()

# Point indices and coordinates for the two triangles forming the
# triangulation:

tri.simplices
# array([[3, 2, 0],
# [3, 1, 0]], dtype=int32)
points[tri.simplices]
# array([[[ 1. ,  1. ],
# [ 1. ,  0. ],
# [ 0. ,  0. ]],
# [[ 1. ,  1. ],
# [ 0. ,  1.1],
# [ 0. ,  0. ]]])

# Triangle 0 is the only neighbor of triangle 1, and it's opposite to
# vertex 1 of triangle 1:

tri.neighbors[1]
# array([-1,  0, -1], dtype=int32)
points[tri.simplices[1,1]]
# array([ 0. ,  1.1])

# We can find out which triangle points are in:

p = np.array([(0.1, 0.2), (1.5, 0.5)])
tri.find_simplex(p)
# array([ 1, -1], dtype=int32)

# We can also compute barycentric coordinates in triangle 1 for
# these points:

b = tri.transform[1,:2].dot(p - tri.transform[1,2])
np.c_[b, 1 - b.sum(axis=1)]
# array([[ 0.1       ,  0.2       ,  0.7       ],
# [ 1.27272727,  0.27272727, -0.54545455]])

# The coordinates for the first point are all positive, meaning it
# is indeed inside the triangle.
