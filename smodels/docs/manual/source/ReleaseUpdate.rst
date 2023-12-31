.. index:: What's New

.. |element| replace:: :ref:`element <element>`
.. |elements| replace:: :ref:`elements <element>`
.. |topology| replace:: :ref:`topology <topology>`
.. |topologies| replace:: :ref:`topologies <topology>`
.. |decomposition| replace:: :doc:`decomposition <Decomposition>`
.. |constraint| replace:: :ref:`constraint <ULconstraint>`
.. |constraints| replace:: :ref:`constraints <ULconstraint>`
.. |runSModelS| replace:: :ref:`runSModelS.py <runSModelS>`
.. |database| replace:: :ref:`database <Database>`
.. |Fastlim| replace:: :ref:`Fastlim <addingFastlim>`
.. |output| replace:: :ref:`output <smodelsOutput>`
.. |results| replace:: :ref:`experimental results <ExpResult>`
.. |txnames| replace:: :ref:`txnames <TxName>`
.. |EM| replace:: :ref:`EM-type <EMtype>`
.. |UL| replace:: :ref:`UL-type <ULtype>`
.. |EMr| replace:: :ref:`EM-type result <EMtype>`
.. |ULr| replace:: :ref:`UL-type result <ULtype>`
.. |EMrs| replace:: :ref:`EM-type results <EMtype>`
.. |ULrs| replace:: :ref:`UL-type results <ULtype>`
.. |ExpRes| replace:: :ref:`Experimental Result<ExpResult>`
.. |ExpRess| replace:: :ref:`Experimental Results<ExpResult>`
.. |expres| replace:: :ref:`experimental result<ExpResult>`
.. |express| replace:: :ref:`experimental results<ExpResult>`
.. |Dataset| replace:: :ref:`DataSet<DataSet>`
.. |Datasets| replace:: :ref:`DataSets<DataSet>`
.. |dataset| replace:: :ref:`data set<DataSet>`
.. |datasets| replace:: :ref:`data sets<DataSet>`
.. |parameters| replace:: :ref:`parameters file <parameterFile>`
.. |ssigBRe| replace:: :math:`\sum \sigma \times BR \times \epsilon`
.. |Cpp| replace:: :ref:`C++ Interface<Cpp>`



What's New
==========
Since the publication of SModelS v1.0 in December 2014, the code base
has undergone significant structural changes. 
The major novelties of this release are as follows:

New in Version 1.2.0:
^^^^^^^^^^^^^^^^^^^^^

  * Decomposition and experimental results can include
    non-MET signatures :ref:`final states <final stateOdd>` (e.g. heavy stable charged particles or HSCP)
  * Added :ref:`lifetime reweighting <lifetimeWeight>` at |decomposition| for meta-stable particles
  * Added :ref:`finalState property <final stateOdd>` for Elements
  * Introduction of :ref:`inclusive simplified models <inclusiveSMS>`
  * Inclusion of HSCP results in the database

New in Version 1.1.3:
^^^^^^^^^^^^^^^^^^^^^

  * Support for :ref:`covariance matrices <combineSRs>` and combination of signal regions (see :ref:`combineSR <parameterFileCombineSRs>` in |parameters|)
  * New plotting tool added to smodelsTools (see :ref:`Interactive Plots Maker <interactivePlots>`)
  * Path to particles.py can now be specified in parameters.ini file (see :ref:`model <parameterFileModel>` in |parameters|)
  * Wildcards allowed when selecting analyses, datasets, txnames (see :ref:`analyses <parameterFileAnalyses>`, :ref:`txnames <parameterFileTxnames>` and :ref:`dataselector <parameterFileDataselector>`  in |parameters|) 
  * Option to show individual contribution from topologies to total theory prediction (see :ref:`addTxWeights <parameterFileAddTxWeights>` in |parameters|)
  * URLs are allowed as database paths (see :ref:`path <parameterFilePath>` in |parameters|)
  * Python default changed from python2 to python3
  * Fixed lastUpdate bug, now giving correct date 
  * Changes in pickling (e.g. subpickling, removing redundant zeroes)
  * Added fixpermissions to smodelsTools.py, for system-wide installs (see :ref:`Files Permissions Fixer <permissionsFixer>`)
  * Fixed small issue with pair production of even particles
  * Moved the :ref:`code documentation <CodeDocs>` to the manual
  * Added :ref:`option for installing <phenoInstallation>` within the source folder


New in Version 1.1.2:
^^^^^^^^^^^^^^^^^^^^^

* Database update only, the code is the same as v1.1.1

New in Version 1.1.1:
^^^^^^^^^^^^^^^^^^^^^

* |Cpp|
* Support for pythia8 (see :ref:`Cross Section Calculator <xsecCalc>`)
* improved binary database
* automated SLHA and LHE file detection
* Fix and improvements for missing topologies
* Added SLHA-type output
* Small improvements in interpolation and clustering


New in Version 1.1.0:
^^^^^^^^^^^^^^^^^^^^^

* the inclusion of efficiency maps (see |EMrs|)
* a new and more flexible database format (see :ref:`Database structure <databaseStruct>`)
* inclusion of likelihood and :math:`\chi^2` calculation for |EMrs|
  (see :ref:`likelihood calculation <likelihoodCalc>`)
* extended information on the :ref:`topology coverage <topCoverage>`
* inclusion of a database broswer tool for easy access to the information
  stored in the database (see :ref:`database browser <databaseBrowser>`)
* the database now supports also a more efficient :ref:`binary format <databasePickle>`
* performance improvement for the |decomposition| of the input model
* inclusion of new simplified results to the |database| (including a few 13 TeV results)
* |Fastlim| efficiency maps can now also be used in SModelS


