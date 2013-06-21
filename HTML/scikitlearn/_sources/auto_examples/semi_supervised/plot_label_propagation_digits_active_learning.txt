

.. _example_semi_supervised_plot_label_propagation_digits_active_learning.py:


========================================
Label Propagation digits active learning
========================================

Demonstrates an active learning technique to learn handwritten digits
using label propagation.

We start by training a label propagation model with only 10 labeled points,
then we select the top five most uncertain points to label. Next, we train
with 15 labeled points (original 10 + 5 new ones). We repeat this process
four times to have a model trained with 30 labeled examples.

A plot will appear showing the top 5 most uncertain digits for each iteration
of training. These may or may not contain mistakes, but we will train the next
model with their true labels.


**Python source code:** :download:`plot_label_propagation_digits_active_learning.py <plot_label_propagation_digits_active_learning.py>`

.. literalinclude:: plot_label_propagation_digits_active_learning.py
    :lines: 18-
    