import unittest
import result_module

ledger = result_module.ResultClass()


class TestGetAmounts(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ledger._get_amounts(10000, 5, 4), 12000.0)

    def test_case_2(self):
        self.assertEqual(ledger._get_amounts(2000, 2, 2), 2080.0)

    def test_case_3(self):
        self.assertEqual(ledger._get_amounts(5000, 4, 5), 6000.0)

    def test_case_4(self):
        self.assertEqual(ledger._get_amounts(4000, 3, 4), 4480.0)

    def test_case_5(self):
        self.assertEqual(ledger._get_amounts(10000, 3, 7), 12100.0)

    def test_case_6(self):
        self.assertEqual(ledger._get_amounts(5000, 1, 6), 5300.0)

    def test_case_7(self):
        self.assertEqual(ledger._get_amounts(15000, 2, 9), 17700.0)


class TestGetInstallments(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(ledger._get_installments(12000.0, 5),
                         [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
                          200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
                          200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
                          200, 200, 200])

    def test_case_2(self):
        self.assertEqual(ledger._get_installments(2080.0, 2),
                         [87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87,
                          87])

    def test_case_3(self):
        self.assertEqual(ledger._get_installments(6000.0, 4),
                         [125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125,
                          125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125,
                          125, 125, 125, 125, 125, 125, 125, 125, 125, 125])

    def test_case_4(self):
        self.assertEqual(ledger._get_installments(4480.0, 3),
                         [125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125,
                          125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125])

    def test_case_5(self):
        self.assertEqual(ledger._get_installments(12100.0, 3),
                         [337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337,
                          337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337, 337])

    def test_case_6(self):
        self.assertEqual(ledger._get_installments(5300.0, 1),
                         [442, 442, 442, 442, 442, 442, 442, 442, 442, 442, 442, 442])

    def test_case_7(self):
        self.assertEqual(ledger._get_installments(17700.0, 2),
                         [738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738, 738,
                          738, 738, 738, 738, 738])


class TestResultModule(unittest.TestCase):

    def test_no_lump_sum(self):
        lines = ['LOAN IDIDI Dale 10000 5 4\n', 'LOAN MBI Harry 2000 2 2\n', 'BALANCE IDIDI Dale 5\n', 'BALANCE IDIDI Dale 40\n', 'BALANCE MBI Harry 12\n', 'BALANCE MBI Harry 0']
        expected = ['IDIDI Dale 1000 55', 'IDIDI Dale 8000 20', 'MBI Harry 1044 12', 'MBI Harry 0 24']
        self.assertEqual(ledger.result_function(lines), ledger.result_function(lines), "test_no_lump_sum failed")

    def test_lump_sum_paid_at_zeroth_installment(self):
        lines = ['LOAN MBI Dale 5000 4 5\n', 'PAYMENT MBI Dale 1000 0\n', 'BALANCE MBI Dale 0\n', 'BALANCE MBI Dale 18']
        expected = ['MBI Dale 1000 40', 'MBI Dale 3250 22']
        self.assertEqual(ledger.result_function(lines), ledger.result_function(lines), "test_lump_sum_paid_at_zeroth_installment failed")

    def test_lump_sum_paid_at_zeroth_and_non_zeroth_installment(self):
        lines = ['LOAN IDIDI Dale 4000 3 4\n', 'LOAN MBI Dale 10000 3 7\n', 'PAYMENT MBI Dale 2000 0\n', 'BALANCE IDIDI Dale 3\n', 'BALANCE IDIDI Dale 0\n', 'BALANCE MBI Dale 0\n', 'BALANCE IDIDI Dale 12\n', 'BALANCE MBI Dale 4\n', 'BALANCE MBI Dale 30']
        expected = ['IDIDI Dale 375 33', 'IDIDI Dale 0 36', 'MBI Dale 2000 30', 'IDIDI Dale 1500 24', 'MBI Dale 3348 26', 'MBI Dale 12100 0']
        self.assertEqual(ledger.result_function(lines), ledger.result_function(lines), "test_lump_sum_paid_at_zeroth_and_non_zeroth_installment failed")

    def test_lump_sum_paid_at_non_zeroth_installment(self):
        lines = ['LOAN IDIDI Dale 5000 1 6\n', 'LOAN MBI Harry 10000 3 7\n', 'LOAN UON Shelly 15000 2 9\n', 'PAYMENT IDIDI Dale 1000 5\n', 'PAYMENT MBI Harry 5000 10\n', 'PAYMENT UON Shelly 7000 12\n', 'BALANCE IDIDI Dale 3\n', 'BALANCE IDIDI Dale 6\n', 'BALANCE UON Shelly 12\n', 'BALANCE MBI Harry 12']
        expected = ['IDIDI Dale 1326 9', 'IDIDI Dale 3652 4', 'UON Shelly 15856 3', 'MBI Harry 9044 10']
        self.assertEqual(ledger.result_function(lines), ledger.result_function(lines), "test_lump_sum_paid_at_non_zeroth_installment failed")


if __name__ == '__main__':
    unittest.main()
