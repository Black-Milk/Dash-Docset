

.. _example_linear_model_plot_ridge_path.py:


===========================================================
Plot Ridge coefficients as a function of the regularization
===========================================================

.. currentmodule:: sklearn.linear_model

Shows the effect of collinearity in the coefficients or the
:class:`Ridge`. Each color represents a different feature of the
coefficient vector, and this is displayed as a function of the
regularization parameter.

At the end of the path, as alpha tends toward zero
and the solution tends towards the ordinary least squares, coefficients
exhibit big oscillations.


**Python source code:** :download:`plot_ridge_path.py <plot_ridge_path.py>`

.. literalinclude:: plot_ridge_path.py
    :lines: 17-
    