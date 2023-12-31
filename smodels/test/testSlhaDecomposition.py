#!/usr/bin/env python3

"""
.. module:: testSlhaDecomposition
   :synopsis: Checks slha decomposition, alongside with compression
    
.. moduleauthor:: Wolfgang Waltenberger <wolfgang.waltenberger@gmail.com>
    
"""

import sys
sys.path.insert(0,"../")
from smodels.theory import slhaDecomposer
from smodels.tools.physicsUnits import GeV, fb
import unittest

class SlhaDecompositionTest(unittest.TestCase):
    from smodels.tools.smodelsLogging import logger

    def test(self):
        self.logger.info ( "test decomposition, no compression" )
        """ test the decomposition with no compression """
        slhafile="./testFiles/slha/simplyGluino.slha"
        topos = slhaDecomposer.decompose ( slhafile, .1*fb, False, False, 5.*GeV )
        self.assertEqual ( len(topos), 1 )
        #print len(topos),"topologies."
        topo=topos[0]
        #print topo
        ellist=topo.elementList
        self.assertEqual ( len(ellist), 1 )
        element=ellist[0]
        #print element
        self.assertEqual ( str (element), "[[[q,q]],[[q,q]]]" )
        #print element.weight

if __name__ == "__main__":
    unittest.main()
