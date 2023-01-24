import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Apurva','Sinha',50000)
        self.emp_2 = Employee('Aman','Nilesh',60000)

    def tearDown(self):
        print('tearDown\n')
        pass

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email,'Apurva.Sinha@email.com')
        self.assertEqual(self.emp_2.email,'Aman.Nilesh@email.com')

        self.emp_1.first = 'Anup'
        self.emp_2.first = 'Nilam'

        self.assertEqual(self.emp_1.email,'Anup.Sinha@email.com')
        self.assertEqual(self.emp_2.email,'Nilam.Nilesh@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname,'Apurva Sinha')
        self.assertEqual(self.emp_2.fullname,'Aman Nilesh')

        self.emp_1.first = 'Anup'
        self.emp_2.first = 'Nilam'

        self.assertEqual(self.emp_1.fullname,'Anup Sinha')
        self.assertEqual(self.emp_2.fullname,'Nilam Nilesh')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay,52500)
        self.assertEqual(self.emp_2.pay,63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Sinha/May')
            self.assertEqual(schedule,'Success')

            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Nilesh/June')
            self.assertEqual(schedule,'Bad Respone!')

if __name__ == '__main__':
    unittest.main()