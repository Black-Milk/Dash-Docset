

.. _example_svm_plot_rbf_parameters.py:


==================
RBF SVM parameters
==================

This example illustrates the effect of the parameters `gamma`
and `C` of the rbf kernel SVM.

Intuitively, the `gamma` parameter defines how far the influence
of a single training example reaches, with low values meaning 'far'
and high values meaning 'close'.
The `C` parameter trades off misclassification of training examples
against simplicity of the decision surface. A low C makes
the decision surface smooth, while a high C aims at classifying
all training examples correctly.

Two plots are generated.  The first is a visualization of the
decision function for a variety of parameter values, and the second
is a heatmap of the classifier's cross-validation accuracy as
a function of `C` and `gamma`.


**Python source code:** :download:`plot_rbf_parameters.py <plot_rbf_parameters.py>`

.. literalinclude:: plot_rbf_parameters.py
    :lines: 22-
    