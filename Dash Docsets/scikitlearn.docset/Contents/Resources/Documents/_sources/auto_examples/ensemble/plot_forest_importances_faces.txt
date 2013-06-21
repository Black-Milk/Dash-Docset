

.. _example_ensemble_plot_forest_importances_faces.py:


=================================================
Pixel importances with a parallel forest of trees
=================================================

This example shows the use of forests of trees to evaluate the importance
of the pixels in an image classification task (faces). The hotter the pixel,
the more important.

The code below also illustrates how the construction and the computation
of the predictions can be parallelized within multiple jobs.


**Python source code:** :download:`plot_forest_importances_faces.py <plot_forest_importances_faces.py>`

.. literalinclude:: plot_forest_importances_faces.py
    :lines: 13-
    