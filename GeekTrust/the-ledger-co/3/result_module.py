import calculate_module


class ResultClass(calculate_module.CalculateClass):
    def __init__(self):
        self.installments = dict()
        self.amounts = dict()
        self.payment_array = dict()
        self.res = []

    def __choosen_operation(self, line):
        return f"{line[1]}-{line[2]}"

    def __loan(self, line):
        key = self.__choosen_operation(line)
        self.amounts[key] = self._get_amounts(int(line[3]), int(line[4]), int(line[5]))
        self.installments[key] = self._get_installments(self.amounts[key], int(line[4]))

    def __payment(self, line):
        key = self.__choosen_operation(line)
        self.payment_array[key] = list(map(int, line[3:]))

    def __balance(self, line):
        key = self.__choosen_operation(line)
        amount_paid, remaining_emi = self._get_amount_paid_and_remaining_emi(int(line[3]),
                                                                             self.installments[key],
                                                                             key,
                                                                             self.payment_array,
                                                                             self.amounts)
        self.res.append(' '.join([line[1], line[2], str(int(amount_paid)), str(remaining_emi)]).rstrip())

    def __invalid_op(self, line):
        raise Exception("Invalid operation")

    def __perform_operation(self, line):

        ops = {'LOAN': self.__loan,
               'PAYMENT': self.__payment,
               'BALANCE': self.__balance}

        chosen_operation_function = ops[line[0]]

        return chosen_operation_function(line)

    def result_function(self, lines):
        for i in lines:
            line = i.split()

            self.__perform_operation(line)

        return self.res
