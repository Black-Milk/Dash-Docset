

.. _example_mixture_plot_gmm_classifier.py:


==================
GMM classification
==================

Demonstration of :ref:`gmm` for classification.

Plots predicted labels on both training and held out test data using a
variety of GMM classifiers on the iris dataset.

Compares GMMs with spherical, diagonal, full, and tied covariance
matrices in increasing order of performance.  Although one would
expect full covariance to perform best in general, it is prone to
overfitting on small datasets and does not generalize well to held out
test data.

On the plots, train data is shown as dots, while test data is shown as
crosses. The iris dataset is four-dimensional. Only the first two
dimensions are shown here, and thus some points are separated in other
dimensions.


**Python source code:** :download:`plot_gmm_classifier.py <plot_gmm_classifier.py>`

.. literalinclude:: plot_gmm_classifier.py
    :lines: 22-
    