

.. _example_decomposition_plot_pca_vs_lda.py:


=======================================================
Comparison of LDA and PCA 2D projection of Iris dataset
=======================================================

The Iris dataset represents 3 kind of Iris flowers (Setosa, Versicolour
and Virginica) with 4 attributes: sepal length, sepal width, petal length
and petal width.

Principal Component Analysis (PCA) applied to this data identifies the
combination of attributes (principal components, or directions in the
feature space) that account for the most variance in the data. Here we
plot the different samples on the 2 first principal components.

Linear Discriminant Analysis (LDA) tries to identify attributes that
account for the most variance *between classes*. In particular,
LDA, in constrast to PCA, is a supervised method, using known class labels.


**Python source code:** :download:`plot_pca_vs_lda.py <plot_pca_vs_lda.py>`

.. literalinclude:: plot_pca_vs_lda.py
    :lines: 19-
    