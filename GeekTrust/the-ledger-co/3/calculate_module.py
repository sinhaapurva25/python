import math
import constants_module


class CalculateClass(constants_module.Constants):

    def _get_amounts(self, principal, number_of_years, rate_of_interest):
        rate_of_interest /= self._percentage
        interest = principal * number_of_years * rate_of_interest
        amount = principal + interest

        return amount

    def _get_installments(self, amount, number_of_years):

        total_emis = self._number_of_months_in_an_year * number_of_years

        installment = list()

        if amount % total_emis == 0:
            installment.extend([int(amount // total_emis) for i in range(int(total_emis))])
        else:
            installment.extend([int(amount / total_emis) + 1 for i in range(int(total_emis))])

        return installment

    def _get_amount_paid_and_remaining_emi(self, emi_number, ins, key, payment_array, amounts):
        amount_paid = sum(ins[:emi_number])

        if key in payment_array:
            payment = payment_array[key]
            lump_sum = payment[0]
            emi_number_of_lump_sum = payment[1]

            if emi_number_of_lump_sum <= emi_number:
                amount_paid += lump_sum
        if amount_paid > amounts[key]:
            amount_paid = amounts[key]
        remaining_emi = math.ceil((amounts[key] - amount_paid) / ins[0])

        return amount_paid, remaining_emi

