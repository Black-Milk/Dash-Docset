

.. _example_applications_topics_extraction_with_nmf.py:


========================================================
Topics extraction with Non-Negative Matrix Factorization
========================================================

This is a proof of concept application of Non Negative Matrix
Factorization of the term frequency matrix of a corpus of documents so
as to extract an additive model of the topic structure of the corpus.
The output is a list of topics, each represented as a list of terms
(weights are not shown).

The default parameters (n_samples / n_features / n_topics) should make
the example runnable in a couple of tens of seconds. You can try to
increase the dimensions of the problem, but be aware than the time complexity
is polynomial.



**Python source code:** :download:`topics_extraction_with_nmf.py <topics_extraction_with_nmf.py>`

.. literalinclude:: topics_extraction_with_nmf.py
    :lines: 18-
    