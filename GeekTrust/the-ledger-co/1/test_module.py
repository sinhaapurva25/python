import unittest
import getResults
import getCalculations

class testAmounts(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(getCalculations.Amounts(10000, 5, 4), 12000.0)
    
    def testCase2(self):
        self.assertEqual(getCalculations.Amounts(2000, 2, 2), 2080.0)

    def testCase3(self):
        self.assertEqual(getCalculations.Amounts(5000, 4, 5), 6000.0)

    def testCase4(self):
        self.assertEqual(getCalculations.Amounts(4000, 3, 4), 4480.0)

    def testCase5(self):
        self.assertEqual(getCalculations.Amounts(10000, 3, 7), 12100.0)

    def testCase6(self):
        self.assertEqual(getCalculations.Amounts(5000, 1, 6), 5300.0)

    def testCase7(self):
        self.assertEqual(getCalculations.Amounts(15000, 2, 9), 17700.0)

class testInstallments(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(getCalculations.Installments(12000.0, 5),[200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200])
    
    def testCase2(self):
        self.assertEqual(getCalculations.Installments(2080.0, 2),[87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87])

    def testCase3(self):
        self.assertEqual(getCalculations.Installments(6000.0, 4),[125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125])

    def testCase4(self):
        self.assertEqual(getCalculations.Installments(4480.0, 3),[125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125])

    def testCase5(self):
        self.assertEqual(getCalculations.Installments(12100.0, 3),[337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337])

    def testCase6(self):
        self.assertEqual(getCalculations.Installments(5300.0, 1),[442, 442, 442, 442, 442, 442, 442, 442, 442, 442, 442, 442])

    def testCase7(self):
        self.assertEqual(getCalculations.Installments(17700.0, 2),[738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738])

class testResult(unittest.TestCase):

    def testNoLumpSum(self):
        Lines = ['LOAN IDIDI Dale 10000 5 4\n', 'LOAN MBI Harry 2000 2 2\n', 'BALANCE IDIDI Dale 5\n', 'BALANCE IDIDI Dale 40\n', 'BALANCE MBI Harry 12\n', 'BALANCE MBI Harry 0']
        expected = ['IDIDI Dale 1000 55', 'IDIDI Dale 8000 20', 'MBI Harry 1044 12', 'MBI Harry 0 24']
        self.assertEqual(getResults.Result(Lines),expected,"testNoLumpSum failed")

    def testLumpSumPaidAtZerothInstallment(self):
        Lines = ['LOAN MBI Dale 5000 4 5\n', 'PAYMENT MBI Dale 1000 0\n', 'BALANCE MBI Dale 0\n', 'BALANCE MBI Dale 18']
        expected = ['MBI Dale 1000 40', 'MBI Dale 3250 22']
        self.assertEqual(getResults.Result(Lines),expected,"testLumpSumPaidAtZerothInstallment failed")

    def testLumpSumPaidAtZerothAndNonZerothInstallment(self):
        Lines = ['LOAN IDIDI Dale 4000 3 4\n', 'LOAN MBI Dale 10000 3 7\n', 'PAYMENT MBI Dale 2000 0\n', 'BALANCE IDIDI Dale 3\n', 'BALANCE IDIDI Dale 0\n', 'BALANCE MBI Dale 0\n', 'BALANCE IDIDI Dale 12\n', 'BALANCE MBI Dale 4\n', 'BALANCE MBI Dale 30']
        expected = ['IDIDI Dale 375 33', 'IDIDI Dale 0 36', 'MBI Dale 2000 30', 'IDIDI Dale 1500 24', 'MBI Dale 3348 26', 'MBI Dale 12100 0']
        self.assertEqual(getResults.Result(Lines),expected,"testLumpSumPaidAtZerothAndNonZerothInstallment failed")

    def testLumpSumPaidAtNonZerothInstallment(self):
        Lines = ['LOAN IDIDI Dale 5000 1 6\n', 'LOAN MBI Harry 10000 3 7\n', 'LOAN UON Shelly 15000 2 9\n', 'PAYMENT IDIDI Dale 1000 5\n', 'PAYMENT MBI Harry 5000 10\n', 'PAYMENT UON Shelly 7000 12\n', 'BALANCE IDIDI Dale 3\n', 'BALANCE IDIDI Dale 6\n', 'BALANCE UON Shelly 12\n', 'BALANCE MBI Harry 12']
        expected = ['IDIDI Dale 1326 9', 'IDIDI Dale 3652 4', 'UON Shelly 15856 3', 'MBI Harry 9044 10']
        self.assertEqual(getResults.Result(Lines),expected,"testLumpSumPaidAtNonZerothInstallment failed")

if __name__=='__main__':
    unittest.main()