

.. _example_cluster_plot_kmeans_digits.py:


===========================================================
A demo of K-Means clustering on the handwritten digits data
===========================================================

In this example with compare the various initialization strategies for
K-means in terms of runtime and quality of the results.

As the ground truth is known here, we also apply different cluster
quality metrics to judge the goodness of fit of the cluster labels to the
ground truth.

Cluster quality metrics evaluated (see :ref:`clustering_evaluation` for
definitions and discussions of the metrics):

=========== ========================================================
Shorthand    full name
=========== ========================================================
homo         homogeneity score
compl        completeness score
v-meas       V measure
ARI          adjusted Rand index
AMI          adjusted mutual information
silhouette   silhouette coefficient
=========== ========================================================



**Python source code:** :download:`plot_kmeans_digits.py <plot_kmeans_digits.py>`

.. literalinclude:: plot_kmeans_digits.py
    :lines: 28-
    