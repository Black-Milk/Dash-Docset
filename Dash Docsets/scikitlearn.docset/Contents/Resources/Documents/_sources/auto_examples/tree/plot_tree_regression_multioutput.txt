

.. _example_tree_plot_tree_regression_multioutput.py:


===================================================================
Multi-output Decision Tree Regression
===================================================================

Multi-output regression with :ref:`decision trees <tree>`: the decision tree
is used to predict simultaneously the noisy x and y observations of a circle
given a single underlying feature. As a result, it learns local linear
regressions approximating the circle.

We can see that if the maximum depth of the tree (controlled by the
`max_depth` parameter) is set too high, the decision trees learn too fine
details of the training data and learn from the noise, i.e. they overfit.


**Python source code:** :download:`plot_tree_regression_multioutput.py <plot_tree_regression_multioutput.py>`

.. literalinclude:: plot_tree_regression_multioutput.py
    :lines: 15-
    