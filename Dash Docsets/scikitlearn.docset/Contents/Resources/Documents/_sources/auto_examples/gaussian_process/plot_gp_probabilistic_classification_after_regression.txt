

.. _example_gaussian_process_plot_gp_probabilistic_classification_after_regression.py:


==============================================================================
Gaussian Processes classification example: exploiting the probabilistic output
==============================================================================

A two-dimensional regression exercise with a post-processing allowing for
probabilistic classification thanks to the Gaussian property of the prediction.

The figure illustrates the probability that the prediction is negative with
respect to the remaining uncertainty in the prediction. The red and blue lines
corresponds to the 95% confidence interval on the prediction of the zero level
set.


**Python source code:** :download:`plot_gp_probabilistic_classification_after_regression.py <plot_gp_probabilistic_classification_after_regression.py>`

.. literalinclude:: plot_gp_probabilistic_classification_after_regression.py
    :lines: 17-
    