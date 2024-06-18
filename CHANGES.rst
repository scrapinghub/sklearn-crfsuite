Changes
=======

0.5.0 (2024-06-18)
------------------

* The ``CRF.predict()`` and ``CRF.predict_marginals()`` methods now return a
  numpy array, as expected by newer versions of scikit-learn.

* Fixed the parameters of a call to the
  ``sklearn.metrics.classification_report()`` function from the
  ``flat_classification_report()`` function.

* ``sequence_accuracy_score`` now works with numpy arrays.

0.4.0 (2024-06-18)
------------------

* Dropped official support for Python 3.7 and lower, and added official support
  for Python 3.8 and higher.

* Added support for scikit-learn 0.24.0 and higher.

* Increased minimum versions of dependencies as follows:

  * python-crfsuite: 0.8.3 → 0.9.7
  * scikit-learn: 0.24.0
  * tabulate: 0.4.2

* Internal changes: enabled GitHub Actions for CI, added a tox environment for
  minimum supported versions of dependencies, applied automatic code cleanups.

0.3.6 (2017-06-22)
------------------

* added ``sklearn_crfsuite.metrics.flat_recall_score``.

0.3.5 (2017-03-21)
------------------

* Properly close file descriptor in ``FileResource.cleanup``;
* declare Python 3.6 support, stop testing on Python 3.3.

0.3.4 (2016-11-17)
------------------

* Small formatting fixes.

0.3.3 (2016-03-15)
------------------

* scikit-learn dependency is now optional for sklearn_crfsuite;
  it is required only when you use metrics and scorers;
* added ``metrics.flat_precision_score``.

0.3.2 (2015-12-18)
------------------

* Ignore more errors in ``FileResource.__del__``.

0.3.1 (2015-12-17)
------------------

* Ignore errors in ``FileResource.__del__``.

0.3 (2015-12-17)
----------------

* Added ``sklearn_crfsuite.metrics.sequence_accuracy_score()`` function and
  related ``sklearn_crfsuite.scorers.sequence_accuracy``;
* ``FileResource.__del__`` method made more robust.

0.2 (2015-12-11)
----------------

* **backwards-incompatible**: ``crf.tagger`` attribute is renamed to
  ``crf.tagger_``; when model is not trained accessing this attribute
  no longer raises an exception, its value is set to None instead.

* new CRF attributes available after training:

    * ``classes_``
    * ``size_``
    * ``num_attributes_``
    * ``attributes_``
    * ``state_features_``
    * ``transition_features_``

* Tutorial is added.

0.1 (2015-11-27)
----------------

Initial release.
