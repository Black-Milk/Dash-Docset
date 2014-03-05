

.. _example_gaussian_process_gp_diabetes_dataset.py:


========================================================================
Gaussian Processes regression: goodness-of-fit on the 'diabetes' dataset
========================================================================

This example consists in fitting a Gaussian Process model onto the diabetes
dataset.

The correlation parameters are determined by means of maximum likelihood
estimation (MLE). An anisotropic squared exponential correlation model with a
constant regression model are assumed. We also used a nugget = 1e-2 in order to
account for the (strong) noise in the targets.

We compute then compute a cross-validation estimate of the coefficient of
determination (R2) without reperforming MLE, using the set of correlation
parameters found on the whole dataset.


**Python source code:** :download:`gp_diabetes_dataset.py <gp_diabetes_dataset.py>`

.. literalinclude:: gp_diabetes_dataset.py
    :lines: 21-
    