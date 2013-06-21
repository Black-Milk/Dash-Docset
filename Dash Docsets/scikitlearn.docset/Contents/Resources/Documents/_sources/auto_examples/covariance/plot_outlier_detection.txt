

.. _example_covariance_plot_outlier_detection.py:


==========================================
Outlier detection with several methods.
==========================================

This example illustrates two ways of performing :ref:`outlier_detection`
when the amount of contamination is known:

- based on a robust estimator of covariance, which is assuming that the
  data are Gaussian distributed and performs better than the One-Class SVM
  in that case.

- using the One-Class SVM and its ability to capture the shape of the
  data set, hence performing better when the data is strongly
  non-Gaussian, i.e. with two well-separated clusters;

The ground truth about inliers and outliers is given by the points colors
while the orange-filled area indicates which points are reported as outliers
by each method.

Here, we assume that we know the fraction of outliers in the datasets.
Thus rather than using the 'predict' method of the objects, we set the
threshold on the decision_function to separate out the corresponding
fraction.


**Python source code:** :download:`plot_outlier_detection.py <plot_outlier_detection.py>`

.. literalinclude:: plot_outlier_detection.py
    :lines: 26-
    