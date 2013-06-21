

.. _example_plot_pls.py:


=========================
PLS Partial Least Squares
=========================

Simple usage of various PLS flavor:
- PLSCanonical
- PLSRegression, with multivariate response, a.k.a. PLS2
- PLSRegression, with univariate response, a.k.a. PLS1
- CCA

Given 2 multivariate covarying two-dimensional datasets, X, and Y,
PLS extracts the 'directions of covariance', i.e. the components of each
datasets that explain the most shared variance between both datasets.
This is apparent on the **scatterplot matrix** display: components 1 in
dataset X and dataset Y are maximaly correlated (points lie around the
first diagonal). This is also true for components 2 in both dataset,
however, the correlation across datasets for different components is
weak: the point cloud is very spherical.


**Python source code:** :download:`plot_pls.py <plot_pls.py>`

.. literalinclude:: plot_pls.py
    :lines: 21-
    