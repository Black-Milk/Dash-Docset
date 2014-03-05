

.. _example_imputation.py:


======================================================
Imputing missing values before building an estimator
======================================================

This example shows that imputing the missing values can give better results
than discarding the samples containing any missing value.

Missing values can be replaced by the mean, the median or the most frequent
value using the ``strategy`` hyper-parameter.

Script output:

  Score with the entire dataset = 0.56
  Score without the samples containing missing values = 0.48
  Score after imputation of the missing values = 0.55



**Python source code:** :download:`imputation.py <imputation.py>`

.. literalinclude:: imputation.py
    :lines: 19-
    