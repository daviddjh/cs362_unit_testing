import unittest
import calc

class TestCalc(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(calc.add(2,2),4,"should be equal to 4")
        self.assertEqual(calc.add(2.5,2.5),5,"should be equal to 5")
        self.assertEqual(calc.add(2,9),11,"should be equal to 11")
        with self.assertRaises(TypeError): calc.add(2,"hello")

    def testSub(self):
        self.assertEqual(calc.subtract(2,2),0,"should be equal to 0")
        self.assertEqual(calc.subtract(5,2.5),2.5,"should be equal to 2.5")
        with self.assertRaises(TypeError): calc.subtract(2,"hello")

    def testDiv(self):
        self.assertEqual(calc.divide(2,2),1,"should be equal to 1")
        self.assertEqual(calc.divide(5,2.5),2,"should be equal to 2")
        with self.assertRaises(TypeError): calc.divide(2,"hello")
        with self.assertRaises(ValueError): calc.divide(2,0)

    def testMult(self):
        self.assertEqual(calc.multiply(2,8),16,"should be equal to 16")
        self.assertEqual(calc.multiply(2.5,2),5,"should be equal to 5")
        with self.assertRaises(TypeError): calc.multiply(2,"hello")

if __name__ == "__main__":
    unittest.main()
