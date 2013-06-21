

.. _example_covariance_plot_robust_vs_empirical_covariance.py:


=======================================
Robust vs Empirical covariance estimate
=======================================

The usual covariance maximum likelihood estimate is very sensitive to
the presence of outliers in the data set. In such a case, one would
have better to use a robust estimator of covariance to garanty that
the estimation is resistant to "errorneous" observations in the data
set.

The Minimum Covariance Determinant estimator is a robust,
high-breakdown point (i.e. it can be used to estimate the covariance
matrix of highly contaminated datasets, up to
:math:`rac{n_samples-n_features-1}{2}` outliers) estimator of
covariance. The idea is to find :math:`rac{n_samples+n_features+1}{2}`
observations whose empirical covariance has the smallest determinant,
yielding a "pure" subset of observations from which to compute
standards estimates of location and covariance. After a correction
step aiming at compensating the fact the the estimates were learnt
from only a portion of the initial data, we end up with robust
estimates of the data set location and covariance.

The Minimum Covariance Determinant estimator (MCD) has been introduced
by P.J.Rousseuw in [1].

In this example, we compare the estimation errors that are made when
using three types of location and covariance estimates on contaminated
gaussian distributed data sets:

- The mean and the empirical covariance of the full dataset, which break
  down as soon as there are outliers in the data set
- The robust MCD, that has a low error provided n_samples > 5 * n_features
- The mean and the empirical covariance of the observations that are known
  to be good ones. This can be considered as a "perfect" MCD estimation,
  so one can trust our implementation by comparing to this case.

[1] P. J. Rousseeuw. Least median of squares regression. J. Am
    Stat Ass, 79:871, 1984.
[2] Johanna Hardin, David M Rocke. Journal of Computational and
    Graphical Statistics. December 1, 2005, 14(4): 928-946.



**Python source code:** :download:`plot_robust_vs_empirical_covariance.py <plot_robust_vs_empirical_covariance.py>`

.. literalinclude:: plot_robust_vs_empirical_covariance.py
    :lines: 44-
    