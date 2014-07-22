__author__ = 'jchaudhary'

import unittest
from src import Input

class TestInput(unittest.TestCase):
    def setUp(self):
        self.inputA = Input.Input(r'E:\works')
        self.inputB = Input.Input('E:\works', extensions=['ima','IMA'])
        self.inputC = Input.Input('E:\works', databases=['sql'])
        try:
            self.inputD = Input.Input('not a directory', extensions=['dir'], databases=['mongo'])
        except:
            ValueError

    def testInputA(self):
        self.assertEqual('E:\works', self.inputA.baseDirectory)
        self.assertEqual(Input.CONST_EXTENSIONS, self.inputA.extensions)
        self.assertEqual(Input.CONST_DATABASES, self.inputA.databases)
        print 'testInputA pass'

    def testInputB(self):
        self.assertEqual('E:\works',self.inputB.baseDirectory)
        for ext in self.inputB.extensions:
            self.assertIn(ext, Input.CONST_EXTENSIONS)
        self.assertEqual(Input.CONST_DATABASES, self.inputB.databases)
        print 'testInputB pass'

    def testInputC(self):
        self.assertEqual('E:\works',self.inputC.baseDirectory)
        self.assertEqual(Input.CONST_EXTENSIONS, self.inputC.extensions)
        for db in self.inputC.databases:
            self.assertIn(db, Input.CONST_DATABASES)
        print 'testInputC pass'

    def testInputD(self):
        #self.assertNotEqual('E:\works',self.inputD.baseDirectory)
        #self.assertNotIn(self.inputD.extensions, Input.CONST_EXTENSIONS)
        #self.assertIn(self.inputD.databases, Input.CONST_DATABASES)
        self.assertRaises(ValueError, self.inputD)
        for ext in self.inputD.extensions:
            self.assertNotIn(ext, Input.CONST_EXTENSIONS)

        for db in self.inputD.databases:
            self.assertNotIn(db, Input.CONST_DATABASES)
        print 'testD pass'

    def tearDown(self):
        del self.inputA, self.inputB, self.inputC, self.inputD

if __name__ == '__main__':
    unittest.main()