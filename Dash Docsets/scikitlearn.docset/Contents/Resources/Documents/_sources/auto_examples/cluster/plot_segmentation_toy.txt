

.. _example_cluster_plot_segmentation_toy.py:


===========================================
Spectral clustering for image segmentation
===========================================

In this example, an image with connected circles is generated and
:ref:`spectral_clustering` is used to separate the circles.

In these settings, the spectral clustering approach solves the problem
know as 'normalized graph cuts': the image is seen as a graph of
connected voxels, and the spectral clustering algorithm amounts to
choosing graph cuts defining regions while minimizing the ratio of the
gradient along the cut, and the volume of the region.

As the algorithm tries to balance the volume (ie balance the region
sizes), if we take circles with different sizes, the segmentation fails.

In addition, as there is no useful information in the intensity of the image,
or its gradient, we choose to perform the spectral clustering on a graph
that is only weakly informed by the gradient. This is close to performing
a Voronoi partition of the graph.

In addition, we use the mask of the objects to restrict the graph to the
outline of the objects. In this example, we are interested in
separating the objects one from the other, and not from the background.


**Python source code:** :download:`plot_segmentation_toy.py <plot_segmentation_toy.py>`

.. literalinclude:: plot_segmentation_toy.py
    :lines: 27-
    