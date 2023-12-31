#!/usr/bin/env python3

"""
.. module:: testTheoryPrediction
   :synopsis: Testing the theory prediction.

.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>

"""

from __future__ import print_function
import sys
sys.path.insert(0,"../")
import unittest
from smodels.tools.physicsUnits import fb, GeV
from databaseLoader import database
import inspect
from smodels.theory.theoryPrediction import theoryPredictionsFor
from smodels.theory import slhaDecomposer
from smodels.tools.smodelsLogging import setLogLevel

class IntegrationTest(unittest.TestCase):
    def configureLogger(self):
        import logging.config
        fc= inspect.getabsfile(self.configureLogger).replace ( 
                "testTheoryPrediction.py", "integration.conf" )
        logging.config.fileConfig( fname=fc, disable_existing_loggers=False )

    def predictions(self):
        return { 'ATLAS-SUSY-2013-02': 572.168935 * fb,
                 'CMS-SUS-13-012': 1.73810052766 * fb }

    def predchi2(self):
        return { 'ATLAS-SUSY-2013-02': None,
     #            'CMS-SUS-13-012': 19.9647839329 } ## with 20% signal error
                 'CMS-SUS-13-012': 45.35806410622854 } ## thats with no signal error

    def checkAnalysis(self,expresult,smstoplist):
        expID = expresult.globalInfo.id
        theorypredictions = theoryPredictionsFor(expresult, smstoplist)
        defpreds=self.predictions()
        if not theorypredictions:
            print ( "no theory predictions for",expresult,"??" )
            sys.exit(-1)
        for pred in theorypredictions:
            predval=pred.xsection.value 
            defpredval = defpreds[expID]
            self.assertAlmostEqual( predval.asNumber(fb), defpredval.asNumber (fb) )
            pred.computeStatistics( marginalize=True, deltas_rel=0. )
            if pred.chi2 != self.predchi2()[expID]:
                self.assertAlmostEqual(pred.chi2/self.predchi2()[expID], 1.0, 1 )


    def testIntegration(self):
        slhafile = './testFiles/slha/simplyGluino.slha'
        self.configureLogger()
        smstoplist = slhaDecomposer.decompose(slhafile, .1*fb, doCompress=True,
                doInvisible=True, minmassgap=5.*GeV)
        listofanalyses = database.getExpResults( 
                analysisIDs= [ "ATLAS-SUSY-2013-02", "CMS-SUS-13-012" ], 
                txnames = [ "T1" ] )
        if type(listofanalyses) != list:
            listofanalyses= [ listofanalyses] 
        for analysis in listofanalyses:
            self.checkAnalysis(analysis,smstoplist)
    
    def checkPrediction(self,slhafile,expID,expectedValues):
        self.configureLogger()
        smstoplist = slhaDecomposer.decompose(slhafile, 0.*fb, doCompress=True,
                doInvisible=True, minmassgap=5.*GeV)
        expresults = database.getExpResults(analysisIDs= expID)
        for expresult in expresults:
            theorypredictions = theoryPredictionsFor(expresult, smstoplist)
            for pred in theorypredictions:
                predval=pred.xsection.value 
                expval = expectedValues.pop()
                delta = expval*0.01
                self.assertAlmostEqual(predval.asNumber(fb), expval,delta=delta)
        
        self.assertTrue(len(expectedValues) == 0)
            
    def testHSCPPredictions(self):
        setLogLevel('error')
        expID = ["CMS-EXO-13-006"]
        
        #Test long-lived case:
        slhafile = './testFiles/slha/hscpTest_long.slha'
        expValue = [0.0743]
        self.checkPrediction(slhafile, expID, expValue)

        #Test displaced case:
        slhafile = './testFiles/slha/hscpTest_mid.slha'
        expValue = [2.20e-7]
        self.checkPrediction(slhafile, expID, expValue)


        #Test short-lived case:
        slhafile = './testFiles/slha/hscpTest_short.slha'
        expValue = [5.98e-10]
        self.checkPrediction(slhafile, expID, expValue)


if __name__ == "__main__":
    unittest.main()
