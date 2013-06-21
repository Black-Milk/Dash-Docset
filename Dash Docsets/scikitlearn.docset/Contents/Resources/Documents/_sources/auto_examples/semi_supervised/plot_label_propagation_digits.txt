

.. _example_semi_supervised_plot_label_propagation_digits.py:


===================================================
Label Propagation digits: Demonstrating performance
===================================================

This example demonstrates the power of semisupervised learning by
training a Label Spreading model to classify handwritten digits
with sets of very few labels.

The handwritten digit dataset has 1797 total points. The model will
be trained using all points, but only 30 will be labeled. Results
in the form of a confusion matrix and a series of metrics over each
class will be very good.

At the end, the top 10 most uncertain predictions will be shown.


**Python source code:** :download:`plot_label_propagation_digits.py <plot_label_propagation_digits.py>`

.. literalinclude:: plot_label_propagation_digits.py
    :lines: 17-
    