

.. _example_plot_digits_pipe.py:


=========================================================
Pipelining: chaining a PCA and a logistic regression
=========================================================

The PCA does an unsupervised dimensionality reduction, while the logistic
regression does the prediction.

We use a GridSearchCV to set the dimensionality of the PCA



**Python source code:** :download:`plot_digits_pipe.py <plot_digits_pipe.py>`

.. literalinclude:: plot_digits_pipe.py
    :lines: 15-
    