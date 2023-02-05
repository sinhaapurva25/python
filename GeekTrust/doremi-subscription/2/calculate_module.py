import constants_module


class CalculateClass(constants_module.Constants):

    def _suffix(self, num):
        return f'{self._zero}{str(num)}' if num < self._ten else str(num)

    def _do_nothing(self):
        pass

    def _days(self, calendar, number_of_days, month, year):
        for j in range(self._one, number_of_days + self._one):
            dd = self._suffix(j)
            mm = self._suffix(month)
            calendar.append('-'.join([dd, mm, str(year)]))
        return calendar

    def _leap_year(self, yy):
        return (yy % self._leap_year_condition_one == self._zero) or (
                yy % self._leap_year_condition_two != self._zero) and (
                yy % self._leap_year_condition_three == self._zero)

    def _get_number_of_days(self, *inputs):
        pass

    def _generate_calendar(self, yy):
        days_arr = list()
        calendar = list()
        for i in range(self._one, self._number_of_months + self._one):

            case = ''.join(list(map(str, map(int, [i in self._odd_months,
                                                   i in self._even_months,
                                                   self._leap_year(yy)
                                                   ]
                                             )
                                    )
                                )
                           )
            ops = {self._is_odd: self._max_days_in_odd_months,
                   self._is_even: self._max_days_in_even_months,
                   self._leap_feb: self._max_days_in_leap_feb}
            try:
                number_of_days = ops[case]
            except Exception:
                number_of_days = self._max_days_in_non_leap_feb

            self._days(calendar, number_of_days, i, yy)

            days_arr.append(number_of_days)

        yy += self._one

        number_of_days = self._max_days_in_odd_months
        self._days(calendar, number_of_days, self._one, yy)
        days_arr.append(number_of_days)

        number_of_days = self._max_days_in_leap_feb if self._leap_year(yy) else self._max_days_in_non_leap_feb

        self._days(calendar, number_of_days, self._two, yy)
        days_arr.append(number_of_days)

        number_of_days = self._max_days_in_odd_months
        self._days(calendar, number_of_days, self._three, yy)
        days_arr.append(number_of_days)

        return days_arr, calendar

    def _get_case_func(self, case_boolean, func1, func2, *inputs):
        case = str(case_boolean)
        ops = {self._true_case: func1, self._false_case: func2}
        chosen_operation_function = ops[case]
        return chosen_operation_function

    def _valid_number_of_months(self, dd, mm, yy):
        valid_date_boolean = True
        if mm in self._odd_months:
            if dd > self._max_days_in_odd_months:
                valid_date_boolean = False
        elif mm in self._even_months:
            if dd > self._max_days_in_even_months:
                valid_date_boolean = False
        else:
            if self._leap_year(yy):
                if dd > self._max_days_in_leap_feb:
                    valid_date_boolean = False
            else:
                if dd > self._max_days_in_non_leap_feb:
                    valid_date_boolean = False
        return valid_date_boolean

    def _valid_date(self, dd, mm, yy):

        valid_date_boolean = mm <= self._number_of_months

        if mm <= self._number_of_months:
            if mm in self._odd_months:
                if dd > self._max_days_in_odd_months:
                    valid_date_boolean = False
            elif mm in self._even_months:
                if dd > self._max_days_in_even_months:
                    valid_date_boolean = False
            else:
                if self._leap_year(yy):
                    if dd > self._max_days_in_leap_feb:
                        valid_date_boolean = False
                else:
                    if dd > self._max_days_in_non_leap_feb:
                        valid_date_boolean = False
        return valid_date_boolean
