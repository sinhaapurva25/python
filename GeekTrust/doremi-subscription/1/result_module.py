import calculate_module


class ResultClass(calculate_module.CalculateClass):
    def __init__(self):
        self.date_index = 1
        self.first_line_index = 0

        self.invalid_date_string = 'INVALID_DATE'

        self.categories = {'MUSIC': 0, 'VIDEO': 0, 'PODCAST': 0}
        self.top_up_categories = {'FOUR_DEVICE': 0, 'TEN_DEVICE': 0}
        self.renewal_amount = 0
        self.duplicate_flag = 0

    def result_function(self, lines):
        res = list()

        dd, mm, yy = list(map(int, lines[self.first_line_index].split(" ")[self.date_index].split("-")))
        valid_date_boolean = self._valid_date(dd, mm, yy)

        if valid_date_boolean:
            days_arr, calendar = self._generate_calendar(yy)
            present_day = sum(days_arr[:mm - 1]) + dd - 1
        else:
            res.append(self.invalid_date_string)

        for i in lines[1:]:
            line = i.strip().split(" ")  # remove '\n' from plan

            if 'ADD' in line[0]:  # if line[0].split("_")[0] == 'ADD':
                task, category, plan = line

                if valid_date_boolean:

                    if category in self.categories.keys():

                        if self.categories[category] == 0:
                            self.categories[category] += 1
                            self.renewal_amount += self._price[category + ' ' + plan]

                            if plan == 'PREMIUM':
                                next_date = calendar[present_day + days_arr[mm - 1] + days_arr[mm] + days_arr[mm + 1] - 10]

                            else:
                                next_date = calendar[present_day + days_arr[mm - 1] - 10]

                            res.append('RENEWAL_REMINDER ' + category + ' ' + next_date)

                        else:
                            self.duplicate_flag += 1
                            res.append(task + '_FAILED DUPLICATE_' + 'CATEGORY')

                    elif category in self.top_up_categories.keys():

                        if self.top_up_categories[category] == 0:
                            self.top_up_categories[category] += 1
                            self.renewal_amount += self._price[category] * int(plan)

                        else:
                            self.duplicate_flag += 1
                            res.append(task + '_FAILED DUPLICATE_' + 'TOPUP')

                else:
                    res.append(task + '_FAILED' + ' ' + self.invalid_date_string)

            else:

                if valid_date_boolean:
                    res.append('RENEWAL_AMOUNT ' + str(self.renewal_amount))

                else:
                    res.append('SUBSCRIPTIONS_NOT_FOUND')

        if self.duplicate_flag:
            return [' '.join(x) for _, x in sorted(zip(self._arrange_res_by_key, [i.split() for i in res]))]
        else:
            return res
