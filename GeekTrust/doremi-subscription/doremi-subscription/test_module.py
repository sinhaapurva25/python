import unittest
import subscription

class testLeapYear(unittest.TestCase):
    
    def testYears(self):
        self.assertEqual(subscription.leapYear(1900),False,"1900 is not a leap year")
        self.assertEqual(subscription.leapYear(2000),True,"2000 is not a leap year")
        self.assertEqual(subscription.leapYear(2016),True,"2016 is not a leap year")
        self.assertEqual(subscription.leapYear(2021),False,"2021 is not a leap year")

class testDate(unittest.TestCase):

    def testCorrectDates(self):
        self.assertEqual(subscription.validDate(5,2,2022),True,"CorrectDates-A failed")
        self.assertEqual(subscription.validDate(8,12,2019),True,"CorrectDates-B failed")
        self.assertEqual(subscription.validDate(25,7,2021),True,"CorrectDates-C failed")
        self.assertEqual(subscription.validDate(20,10,2022),True,"CorrectDates-D failed")

    def testIncorrectMonths(self):
        self.assertEqual(subscription.validDate(10, 21, 2022),False,"CaseIncorrectMonths-A failed")

    def testFebruaryDays(self):
        self.assertEqual(subscription.validDate(28,2,2021),True,"CaseFebruaryDays-A failed")
        self.assertEqual(subscription.validDate(29,2,2021),False,"CaseFebruaryDays-B failed")
        self.assertEqual(subscription.validDate(29,2,2020),True,"CaseFebruaryDays-C failed")
        self.assertEqual(subscription.validDate(30,2,2020),False,"CaseFebruaryDays-D failed")

    def testOddMonths(self):
        self.assertEqual(subscription.validDate(31,1,2021),True,"CaseOddMonths-A failed")
        self.assertEqual(subscription.validDate(32,1,2021),False,"CaseOddMonths-B failed")

    def testEvenMonths(self):
        self.assertEqual(subscription.validDate(30,4,2021),True,"CaseOddMonths-A failed")
        self.assertEqual(subscription.validDate(31,4,2021),False,"CaseOddMonths-B failed")


class testCalculate(unittest.TestCase):

    def testCaseOne(self):
        Lines =  ['START_SUBSCRIPTION 05-02-2022\n', 'ADD_SUBSCRIPTION MUSIC PERSONAL\n', 'ADD_SUBSCRIPTION VIDEO PREMIUM\n', 'ADD_SUBSCRIPTION PODCAST FREE\n', 'ADD_TOPUP FOUR_DEVICE 2\n', 'PRINT_RENEWAL_DETAILS']
        expected = ['RENEWAL_REMINDER MUSIC 23-02-2022', 'RENEWAL_REMINDER VIDEO 25-04-2022', 'RENEWAL_REMINDER PODCAST 23-02-2022', 'RENEWAL_AMOUNT 700']
        self.assertEqual(subscription.calculate(Lines),expected,"testCaseOne failed")

    def testCaseTwo(self):
        Lines = ['START_SUBSCRIPTION 08-12-2019\n', 'ADD_SUBSCRIPTION MUSIC PREMIUM\n', 'ADD_SUBSCRIPTION PODCAST FREE\n', 'ADD_TOPUP TEN_DEVICE 3\n', 'PRINT_RENEWAL_DETAILS']
        expected = ['RENEWAL_REMINDER MUSIC 27-02-2020', 'RENEWAL_REMINDER PODCAST 29-12-2019', 'RENEWAL_AMOUNT 550']
        self.assertEqual(subscription.calculate(Lines),expected,"testCaseTwo failed")

    def testCaseThree(self):
        Lines = ['START_SUBSCRIPTION 25-07-2021\n', 'ADD_SUBSCRIPTION MUSIC PREMIUM\n', 'ADD_SUBSCRIPTION VIDEO PREMIUM\n', 'ADD_SUBSCRIPTION PODCAST PERSONAL\n', 'PRINT_RENEWAL_DETAILS']
        expected = ['RENEWAL_REMINDER MUSIC 15-10-2021', 'RENEWAL_REMINDER VIDEO 15-10-2021', 'RENEWAL_REMINDER PODCAST 15-08-2021', 'RENEWAL_AMOUNT 850']
        self.assertEqual(subscription.calculate(Lines),expected,"testCaseThree failed")

    def testCaseFour(self):
        Lines = ['START_SUBSCRIPTION 10-21-2022\n', 'ADD_SUBSCRIPTION MUSIC PERSONAL\n', 'ADD_SUBSCRIPTION MUSIC PREMIUM\n', 'ADD_TOPUP TEN_DEVICE 3\n', 'PRINT_RENEWAL_DETAILS']
        expected = ['INVALID_DATE', 'ADD_SUBSCRIPTION_FAILED INVALID_DATE', 'ADD_SUBSCRIPTION_FAILED INVALID_DATE', 'ADD_TOPUP_FAILED INVALID_DATE', 'SUBSCRIPTIONS_NOT_FOUND']
        self.assertEqual(subscription.calculate(Lines),expected,"testCaseFour failed")

    def testCaseFive(self):
        Lines = ['START_SUBSCRIPTION 20-10-2022\n', 'ADD_SUBSCRIPTION MUSIC PERSONAL\n', 'ADD_SUBSCRIPTION MUSIC PREMIUM\n', 'ADD_TOPUP TEN_DEVICE 1\n', 'ADD_TOPUP TEN_DEVICE 1\n', 'PRINT_RENEWAL_DETAILS']
        expected = ['ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY', 'ADD_TOPUP_FAILED DUPLICATE_TOPUP', 'RENEWAL_REMINDER MUSIC 10-11-2022', 'RENEWAL_AMOUNT 200']
        self.assertEqual(subscription.calculate(Lines),expected,"testCaseFive failed")