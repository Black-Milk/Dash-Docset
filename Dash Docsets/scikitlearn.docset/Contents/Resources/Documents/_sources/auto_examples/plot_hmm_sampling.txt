

.. _example_plot_hmm_sampling.py:


==================================
Demonstration of sampling from HMM
==================================

This script shows how to sample points from a Hiden Markov Model (HMM):
we use a 4-components with specified mean and covariance.

The plot show the sequence of observations generated with the transitions
between them. We can see that, as specified by our transition matrix,
there are no transition between component 1 and 3.


**Python source code:** :download:`plot_hmm_sampling.py <plot_hmm_sampling.py>`

.. literalinclude:: plot_hmm_sampling.py
    :lines: 13-
    