from scipy.spatial import KDTree
points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
                   [2, 0], [2, 1], [2, 2]])
tree = KDTree(points)
tree.query([0.1, 0.1])
# (0.14142135623730953, 0)

# So the point ``(0.1, 0.1)`` belongs to region ``0``. In color:

x = np.linspace(-0.5, 2.5, 31)
y = np.linspace(-0.5, 2.5, 33)
xx, yy = np.meshgrid(x, y)
xy = np.c_[xx.ravel(), yy.ravel()]
import matplotlib.pyplot as plt
plt.pcolor(x, y, tree.query(xy)[1].reshape(33, 31))
plt.plot(points[:,0], points[:,1], 'ko')
plt.show()

# This does not, however, give the Voronoi diagram as a geometrical
# object.

# The representation in terms of lines and points can be again
# obtained via the Qhull wrappers in `scipy.spatial`:

from scipy.spatial import Voronoi
vor = Voronoi(points)
vor.vertices
# array([[ 0.5,  0.5],
# [ 1.5,  0.5],
# [ 0.5,  1.5],
# [ 1.5,  1.5]])

# The Voronoi vertices denote the set of points forming the polygonal
# edges of the Voronoi regions. In this case, there are 9 different
# regions:

vor.regions
# [[-1, 0], [-1, 1], [1, -1, 0], [3, -1, 2], [-1, 3], [-1, 2], [3, 1, 0, 2], [2, -1, 0], [3, -1, 1]]

# Negative value ``-1`` again indicates a point at infinity. Indeed,
# only one of the regions, ``[3, 1, 0, 2]``, is bounded. Note here that
# due to similar numerical precision issues as in Delaunay triangulation
# above, there may be fewer Voronoi regions than input points.

# The ridges (lines in 2-D) separating the regions are described as a
# similar collection of simplices as the convex hull pieces:

vor.ridge_vertices
# [[-1, 0], [-1, 0], [-1, 1], [-1, 1], [0, 1], [-1, 3], [-1, 2], [2, 3], [-1, 3], [-1, 2], [0, 2], [1, 3]]

# These numbers indicate indices of the Voronoi vertices making up the
# line segments. ``-1`` is again a point at infinity --- only four of
# the 12 lines is a bounded line segment while the others extend to
# infinity.

# The Voronoi ridges are perpendicular to lines drawn between the
# input points. Which two points each ridge corresponds to is also
# recorded:

vor.ridge_points
# array([[0, 3],
# [0, 1],
# [6, 3],
# [6, 7],
# [3, 4],
# [5, 8],
# [5, 2],
# [5, 4],
# [8, 7],
# [2, 1],
# [4, 1],
# [4, 7]], dtype=int32)

# This information, taken together, is enough to construct the full
# diagram.

# We can plot it as follows. First the points and the Voronoi vertices:

plt.plot(points[:,0], points[:,1], 'o')
plt.plot(vor.vertices[:,0], vor.vertices[:,1], '*')
plt.xlim(-1, 3); plt.ylim(-1, 3)

# Plotting the finite line segments goes as for the convex hull,
# but now we have to guard for the infinite edges:

for simplex in vor.ridge_vertices:
    simplex = np.asarray(simplex)
    if np.all(simplex >= 0):
        plt.plot(vor.vertices[simplex,0], vor.vertices[simplex,1], 'k-')

# The ridges extending to infinity require a bit more care:

center = points.mean(axis=0)
for pointidx, simplex in zip(vor.ridge_points, vor.ridge_vertices):
    simplex = np.asarray(simplex)
    if np.any(simplex < 0):
        i = simplex[simplex >= 0][0] # finite end Voronoi vertex
        t = points[pointidx[1]] - points[pointidx[0]] # tangent
        t /= np.linalg.norm(t)
        n = np.array([-t[1], t[0]]) # normal
        midpoint = points[pointidx].mean(axis=0)
        far_point = vor.vertices[i] + np.sign(np.dot(midpoint - center, n)) * n * 100
        plt.plot([vor.vertices[i,0], far_point[0]],
                 [vor.vertices[i,1], far_point[1]], 'k--')
plt.show()
