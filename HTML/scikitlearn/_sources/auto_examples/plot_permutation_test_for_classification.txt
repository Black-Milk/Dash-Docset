

.. _example_plot_permutation_test_for_classification.py:


=================================================================
Test with permutations the significance of a classification score
=================================================================

In order to test if a classification score is significative a technique
in repeating the classification procedure after randomizing, permuting,
the labels. The p-value is then given by the percentage of runs for
which the score obtained is greater than the classification score
obtained in the first place.



**Python source code:** :download:`plot_permutation_test_for_classification.py <plot_permutation_test_for_classification.py>`

.. literalinclude:: plot_permutation_test_for_classification.py
    :lines: 13-
    