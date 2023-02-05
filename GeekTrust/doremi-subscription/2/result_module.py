import calculate_module


class ResultClass(calculate_module.CalculateClass):
    def __init__(self):
        self.date_index = self._one
        self.first_line_index = self._zero

        self.invalid_date_string = 'INVALID_DATE'

        self.categories = {'MUSIC': self._zero, 'VIDEO': self._zero, 'PODCAST': self._zero}
        self.top_up_categories = {'FOUR_DEVICE': self._zero, 'TEN_DEVICE': self._zero}
        self.renewal_amount = self._zero
        self.duplicate_flag = self._zero

    def __renewal_premium(self, __present_day, __days_arr, __mm):
        return __present_day + __days_arr[__mm - self._one] + __days_arr[__mm] + __days_arr[
            __mm + self._one] - self._ten

    def __renewal_regular(self, __present_day, __days_arr, __mm):
        return __present_day + __days_arr[__mm - self._one] - self._ten

    def __renewal(self, *inputs):
        __category, __plan, __present_day, __days_arr, __mm, __calendar, __res = inputs[:-abs(self._one)]

        self.categories[__category] += self._one
        self.renewal_amount += self._price[f'{__category} {__plan}']

        __next_date_index = self._get_case_func(__plan == self._premium, self.__renewal_premium, self.__renewal_regular)(__present_day, __days_arr, __mm)

        __next_date = __calendar[__next_date_index]

        __res.append(f'{self._renewal_reminder} {__category} {__next_date}')

        return __res

    def __failed_duplicate(self, *inputs):
        __res, __task = inputs[-abs(self._two)], inputs[-abs(self._one)]
        self.duplicate_flag += self._one
        __res.append(f'{__task}{self._failed_duplicate_category}')
        return __res

    def __new_category(self, *inputs):
        __category, __plan, __res, __task = inputs
        self.top_up_categories[__category] += self._one
        self.renewal_amount += self._price[__category] * int(__plan)
        return __res

    def __failed_category(self, *inputs):
        __category, __plan, __res, __task = inputs
        self.duplicate_flag += self._one
        __res.append(f'{__task}{self._failed_duplicate_topup}')
        return __res

    def __valid_date_boolean(self, *inputs):
        __category, __plan, __present_day, __days_arr, __mm, __calendar, __res, __task = inputs

        if __category in self.categories.keys():

            __res = self._get_case_func(self.categories[__category] == self._zero, self.__renewal, self.__failed_duplicate)(__category, __plan, __present_day, __days_arr, __mm, __calendar, __res, __task)

        elif __category in self.top_up_categories.keys():

            __res = self._get_case_func(self.top_up_categories[__category] == self._zero, self.__new_category, self.__failed_category)(__category, __plan, __res, __task)

        return __res

    def __invalid_date_boolean(self, *inputs):
        __res, __task = inputs[-abs(self._two)], inputs[-abs(self._one)]
        __res.append(f'{__task}{self._failed} {self.invalid_date_string}')
        return __res

    def __add_subscription(self, *inputs):
        __res, __valid_date_boolean, __line, __present_day, __days_arr, __mm, __calendar = inputs

        __task, __category, __plan = __line

        __res = self._get_case_func(__valid_date_boolean, self.__valid_date_boolean, self.__invalid_date_boolean)(__category, __plan, __present_day, __days_arr, __mm, __calendar, __res, __task)

        return __res

    def __command(self, *inputs):
        __res, __valid_date_boolean, remaining_inputs = inputs[self._zero], inputs[self._one], inputs[self._two:]

        if __valid_date_boolean:
            __res.append(f'{self._renewal_amount} {str(self.renewal_amount)}')
            return __res
        __res.append(f'{self._subscriptions_not_found}')
        return __res

    def __valid_date_string(self, *inputs):
        dd, mm, yy, res = inputs
        days_arr, calendar = self._generate_calendar(yy)
        present_day = sum(days_arr[:mm - self._one]) + dd - self._one
        return days_arr, calendar, present_day, res

    def __invalid_date_string(self, *inputs):
        days_arr, calendar, present_day = [self._zero, self._zero, self._zero]
        res = inputs[-abs(self._one)]
        res.append(self.invalid_date_string)
        return days_arr, calendar, present_day, res

    def result_function(self, lines):
        res = list()

        dd, mm, yy = list(map(int, lines[self.first_line_index].split(" ")[self.date_index].split("-")))
        valid_date_boolean = self._valid_date(dd, mm, yy)

        days_arr, calendar, present_day, res = self._get_case_func(valid_date_boolean, self.__valid_date_string, self.__invalid_date_string)(dd, mm, yy, res)

        for i in lines[self._one:]:
            line = i.strip().split(" ")

            res = self._get_case_func(self._add in line[self._zero], self.__add_subscription, self.__command)(res, valid_date_boolean, line, present_day, days_arr, mm, calendar)

        if self.duplicate_flag:
            return [' '.join(x) for _, x in sorted(zip(self._arrange_res_by_key, [i.split() for i in res]))]

        return res
