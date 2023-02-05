import constants_module


class CalculateClass(constants_module.Constants):
    def _leap_year(self, yy):
        return (yy % self._leap_year_condition_one == 0) or (yy % self._leap_year_condition_two != 0) and (
                    yy % self._leap_year_condition_three == 0)

    def _days(self, calendar, number_of_days, month, year):
        for j in range(1, number_of_days + 1):
            day = ""
            if j < 10:
                day = day + '0' + str(j)
            else:
                day = day + str(j)
            if month < 10:
                day = day + '-' + '0' + str(month) + '-'
            else:
                day = day + '-' + str(month) + '-'
            day = day + str(year)
            calendar.append(day)
        return calendar

    def _generate_calendar(self, yy):
        days_arr = list()
        calendar = list()
        for i in range(1, self._number_of_months + 1):

            if i in self._odd_months:
                number_of_days = self._max_days_in_odd_months
                self._days(calendar, number_of_days, i, yy)

            elif i in self._even_months:
                number_of_days = self._max_days_in_even_months
                self._days(calendar, number_of_days, i, yy)

            else:
                if self._leap_year(yy):
                    number_of_days = self._max_days_in_leap_feb
                else:
                    number_of_days = self._max_days_in_non_leap_feb
                self._days(calendar, number_of_days, i, yy)

            days_arr.append(number_of_days)

        yy += 1

        number_of_days = self._max_days_in_odd_months
        self._days(calendar, number_of_days, 1, yy)
        days_arr.append(number_of_days)

        if self._leap_year(yy):
            number_of_days = self._max_days_in_leap_feb
        else:
            number_of_days = self._max_days_in_non_leap_feb
        self._days(calendar, number_of_days, 2, yy)
        days_arr.append(number_of_days)

        number_of_days = self._max_days_in_odd_months
        self._days(calendar, number_of_days, 3, yy)
        days_arr.append(number_of_days)

        return days_arr, calendar

    def _valid_date(self, dd, mm, yy):

        valid_date_boolean = True

        if mm > self._number_of_months:
            valid_date_boolean = False
        else:
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
