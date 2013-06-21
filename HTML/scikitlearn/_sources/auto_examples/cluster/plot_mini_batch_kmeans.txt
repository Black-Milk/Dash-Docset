

.. _example_cluster_plot_mini_batch_kmeans.py:


====================================================================
Comparison of the K-Means and MiniBatchKMeans clustering algorithms
====================================================================

We want to compare the performance of the MiniBatchKMeans and KMeans:
the MiniBatchKMeans is faster, but gives slightly different results (see
:ref:`mini_batch_kmeans`).

We will cluster a set of data, first with KMeans and then with
MiniBatchKMeans, and plot the results.
We will also plot the points that are labelled differently between the two
algorithms.


**Python source code:** :download:`plot_mini_batch_kmeans.py <plot_mini_batch_kmeans.py>`

.. literalinclude:: plot_mini_batch_kmeans.py
    :lines: 15-
    