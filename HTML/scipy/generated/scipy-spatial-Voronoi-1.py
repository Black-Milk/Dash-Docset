# Voronoi diagram for a set of point:

points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
                   [2, 0], [2, 1], [2, 2]])
from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(points)

# Plot it:

import matplotlib.pyplot as plt
voronoi_plot_2d(vor)
plt.show()

# The Voronoi vertices:

vor.vertices
# array([[ 0.5,  0.5],
# [ 1.5,  0.5],
# [ 0.5,  1.5],
# [ 1.5,  1.5]])

# There is a single finite Voronoi region, and four finite Voronoi
# ridges:

vor.regions
# [[], [-1, 0], [-1, 1], [1, -1, 0], [3, -1, 2], [-1, 3], [-1, 2], [3, 2, 0, 1], [2, -1, 0], [3, -1, 1]]
vor.ridge_vertices
# [[-1, 0], [-1, 0], [-1, 1], [-1, 1], [0, 1], [-1, 3], [-1, 2], [2, 3], [-1, 3], [-1, 2], [0, 2], [1, 3]]

# The ridges are perpendicular between lines drawn between the following
# input points:

vor.ridge_points
# array([[0, 1],
# [0, 3],
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
