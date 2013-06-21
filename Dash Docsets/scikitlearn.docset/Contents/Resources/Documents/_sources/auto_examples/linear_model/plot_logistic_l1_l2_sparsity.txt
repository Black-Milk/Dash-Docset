

.. _example_linear_model_plot_logistic_l1_l2_sparsity.py:


==============================================
L1 Penalty and Sparsity in Logistic Regression
==============================================

Comparison of the sparsity (percentage of zero coefficients) of solutions when
L1 and L2 penalty are used for different values of C. We can see that large
values of C give more freedom to the model.  Conversely, smaller values of C
constrain the model more. In the L1 penalty case, this leads to sparser
solutions.

We classify 8x8 images of digits into two classes: 0-4 against 5-9.
The visualization shows coefficients of the models for varying C.


**Python source code:** :download:`plot_logistic_l1_l2_sparsity.py <plot_logistic_l1_l2_sparsity.py>`

.. literalinclude:: plot_logistic_l1_l2_sparsity.py
    :lines: 15-
    