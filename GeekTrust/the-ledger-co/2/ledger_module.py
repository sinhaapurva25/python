import math


class LedgerClass:
    def __init__(self):
        self.number_of_months_in_an_year = 12
        self.percentage = 100

    def get_amounts(self, principal, number_of_years, rate_of_interest):
        rate_of_interest /= self.percentage
        interest = principal * number_of_years * rate_of_interest
        amount = principal + interest

        return amount

    def get_installments(self, amount, number_of_years):

        total_emis = self.number_of_months_in_an_year * number_of_years

        installment = list()

        if amount % total_emis == 0:
            installment.extend([int(amount // total_emis) for i in range(int(total_emis))])
        else:
            installment.extend([int(amount / total_emis) + 1 for i in range(int(total_emis))])

        return installment

    def get_amount_paid_and_remaining_emis(self, emi_number, ins, key, payment_array, amounts):
        amount_paid = sum(ins[:emi_number])

        if key in payment_array:
            payment = payment_array[key]
            lump_sum = payment[0]
            emi_number_of_lump_sum = payment[1]

            if emi_number_of_lump_sum <= emi_number:
                amount_paid += lump_sum
        if amount_paid > amounts[key]:
            amount_paid = amounts[key]
        remaining_emis = math.ceil((amounts[key] - amount_paid) / ins[0])

        return amount_paid, remaining_emis

    def result(self, lines):
        installments = dict()
        amounts = dict()
        payment_array = dict()
        res = []
        for i in lines:
            line = i.split()
            key = line[1] + '-' + line[2]

            if line[0] == 'LOAN':
                amounts[key] = self.get_amounts(int(line[3]), int(line[4]), int(line[5]))
                installments[key] = self.get_installments(amounts[key], int(line[4]))

            if line[0] == 'PAYMENT':
                payment_array[key] = list(map(int, line[3:]))

            if line[0] == 'BALANCE':
                amount_paid, remaining_emis = self.get_amount_paid_and_remaining_emis(int(line[3]),
                                                                                      installments[key],
                                                                                      key,
                                                                                      payment_array,
                                                                                      amounts)
                res.append(' '.join([line[1], line[2], str(int(amount_paid)), str(remaining_emis)]))

        return res
