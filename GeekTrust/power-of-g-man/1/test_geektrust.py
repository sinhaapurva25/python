import unittest
import geektrust

class Testgeektrust(unittest.TestCase):

    def test_1(self):
        s = "SOURCE 5 5 N"
        d = "DESTINATION 3 3"
        p = "PRINT_POWER"
        self.assertEqual(geektrust.calculatePower(5,5,3,3,'N'),150)

    def test_2(self):
        s = "SOURCE 0 0 W"
        d = "DESTINATION 6 6"
        p = "PRINT_POWER"
        self.assertEqual(geektrust.calculatePower(0,0,6,6,'W'),70)

    def test_3(self):
        s = "SOURCE 1 4 W"
        d = "DESTINATION 5 2"
        p = "PRINT_POWER"
        self.assertEqual(geektrust.calculatePower(1,4,5,2,'W'),130)

    def test_4(self):
        s = "SOURCE 5 5 E "
        d = "DESTINATION 1 2"
        p = "PRINT_POWER"
        self.assertEqual(geektrust.calculatePower(5,5,1,2,'E'),120)

    def test_5(self):
        s = "SOURCE 0 5 W"
        d = "DESTINATION 6 1"
        p = "PRINT_POWER"
        self.assertEqual(geektrust.calculatePower(0,5,6,1,'W'),90)

    def test_6(self):
        s = "SOURCE 1 1 S"
        d = "DESTINATION 1 2"
        p = "PRINT_POWER"
        self.assertEqual(geektrust.calculatePower(1,1,1,2,'S'),180)

    def test_7(self):
        s = "SOURCE 3 1 W"
        d = "DESTINATION 5 1"
        p = "PRINT_POWER"
        self.assertEqual(geektrust.calculatePower(3,1,5,1,'W'),170)

if __name__=='__main__':
    unittest.main()