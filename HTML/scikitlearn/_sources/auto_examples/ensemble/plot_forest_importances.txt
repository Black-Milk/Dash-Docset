

.. _example_ensemble_plot_forest_importances.py:


=========================================
Feature importances with forests of trees
=========================================

This examples shows the use of forests of trees to evaluate the importance of
features on an artificial classification task. The red bars are the feature
importances of the forest, along with their inter-trees variability.

As expected, the plot suggests that 3 features are informative, while the
remaining are not.


**Python source code:** :download:`plot_forest_importances.py <plot_forest_importances.py>`

.. literalinclude:: plot_forest_importances.py
    :lines: 13-
    