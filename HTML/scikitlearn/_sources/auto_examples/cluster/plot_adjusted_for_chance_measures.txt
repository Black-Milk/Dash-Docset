

.. _example_cluster_plot_adjusted_for_chance_measures.py:


==========================================================
Adjustment for chance in clustering performance evaluation
==========================================================

The following plots demonstrate the impact of the number of clusters and
number of samples on various clustering performance evaluation metrics.

Non-adjusted measures such as the V-Measure show a dependency between
the number of clusters and the number of samples: the mean V-Measure
of random labeling increases signicantly as the number of clusters is
closer to the total number of samples used to compute the measure.

Adjusted for chance measure such as ARI display some random variations
centered around a mean score of 0.0 for any number of samples and
clusters.

Only adjusted measures can hence safely be used as a consensus index
to evaluate the average stability of clustering algorithms for a given
value of k on various overlapping sub-samples of the dataset.



**Python source code:** :download:`plot_adjusted_for_chance_measures.py <plot_adjusted_for_chance_measures.py>`

.. literalinclude:: plot_adjusted_for_chance_measures.py
    :lines: 23-
    