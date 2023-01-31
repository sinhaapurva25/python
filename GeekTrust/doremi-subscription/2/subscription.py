# defining global variables
numberOfMonths = 12
oddMonths = [1, 3, 5, 7, 8, 10, 12]
maxDaysInOddMonths = 31
evenMonths = [4, 6, 9, 11]
maxDaysInEvenMonths = 30
leapYearConditionOne = 400
leapYearConditionTwo = 100
leapYearConditionThree = 4
maxDaysInLeapFeb = 29
maxDaysInNonLeapFeb = 28

price = {'MUSIC FREE': 0,
             'MUSIC PERSONAL': 100,
             'MUSIC PREMIUM': 250,
             'VIDEO FREE': 0,
             'VIDEO PERSONAL': 200,
             'VIDEO PREMIUM': 500,
             'PODCAST FREE': 0,
             'PODCAST PERSONAL': 100,
             'PODCAST PREMIUM': 300,
             'FOUR_DEVICE': 50,
             'TEN_DEVICE': 100}

arrangeResByKey =  ['INVALID_DATE',
                    'ADD_SUBSCRIPTION_FAILED',
                    'ADD_TOPUP_FAILED',
                    'SUBSCRIPTIONS_NOT_FOUND',
                    'RENEWAL_REMINDER',
                    'RENEWAL_AMOUNT']


def leapYear(yy):
    return ((yy % leapYearConditionOne == 0) or (yy % leapYearConditionTwo != 0) and (yy % leapYearConditionThree == 0))


def days(calendar, numberOfDays, month, year):
    for j in range(1, numberOfDays+1):
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


def generateCalendar(yy):
    daysArr = list()
    calendar = list()
    for i in range(1,numberOfMonths+1):
        
        if i in oddMonths:
            numberOfDays = maxDaysInOddMonths
            days(calendar, numberOfDays, i, yy)

        elif i in evenMonths:
            numberOfDays = maxDaysInEvenMonths
            days(calendar, numberOfDays, i, yy)

        else:
            if leapYear(yy):
                numberOfDays = maxDaysInLeapFeb
            else:
                numberOfDays = maxDaysInNonLeapFeb
            days(calendar, numberOfDays, i, yy)
        
        daysArr.append(numberOfDays)
    
    yy += 1
    
    numberOfDays = maxDaysInOddMonths
    days(calendar, numberOfDays, 1, yy)
    daysArr.append(numberOfDays)

    if leapYear(yy):
        numberOfDays = maxDaysInLeapFeb
    else:
        numberOfDays = maxDaysInNonLeapFeb
    days(calendar, numberOfDays, 2, yy)
    daysArr.append(numberOfDays)

    numberOfDays = maxDaysInOddMonths
    days(calendar, numberOfDays, 3, yy)
    daysArr.append(numberOfDays)

    return daysArr, calendar


def validDate(dd, mm, yy):

    validDateBoolean = True

    lY = None

    if mm > numberOfMonths:
        validDateBoolean = False
    else:
        if mm in oddMonths:
            if dd > maxDaysInOddMonths:
                validDateBoolean = False
        elif mm in evenMonths:
            if dd > maxDaysInEvenMonths:
                validDateBoolean = False
        else:
            lY = leapYear(yy)
            if lY:
                if dd > maxDaysInLeapFeb:
                    validDateBoolean = False
            else:
                if dd > maxDaysInNonLeapFeb:
                    validDateBoolean = False
    return validDateBoolean


def calculate(Lines):
    res = list()
    
    dateIndex = 1
    firstLineIndex = 0
    dd, mm, yy = list(map(int, Lines[firstLineIndex].split(" ")[dateIndex].split("-")))
    validDateBoolean = validDate(dd, mm, yy)
    
    invalidDateString = 'INVALID_DATE'
    if validDateBoolean:
        daysArr, calendar = generateCalendar(yy)
        presentDay = sum(daysArr[:mm-1]) + dd -1
    else:
        res.append(invalidDateString)

    Categories = {'MUSIC':0, 'VIDEO':0, 'PODCAST':0}
    topUpCategories = {'FOUR_DEVICE':0, 'TEN_DEVICE':0}
    renewalAmount = 0
    duplicateFlag = 0
    
    for i in Lines[1:]:
        line = i.strip().split(" ")# remove '\n' from plan
        
        if 'ADD' in line[0]:# if line[0].split("_")[0] == 'ADD':
            task, category, plan = line

            if validDateBoolean:

                if category in Categories.keys():
                    
                    if Categories[category] == 0:
                        Categories[category] += 1
                        renewalAmount += price[category+' '+plan]

                        if plan == 'PREMIUM':
                            nextDate = calendar[presentDay+daysArr[mm-1]+daysArr[mm]+daysArr[mm+1]-10]
                            
                        else:
                            nextDate = calendar[presentDay+daysArr[mm-1]-10]
                        
                        res.append('RENEWAL_REMINDER '+ category + ' '+ nextDate)
                    
                    else:
                        duplicateFlag += 1
                        res.append(task +'_FAILED DUPLICATE_' + 'CATEGORY')
                
                elif category in topUpCategories.keys():
                    
                    if topUpCategories[category] == 0:
                        topUpCategories[category] += 1
                        renewalAmount += price[category]*int(plan)

                    else:
                        duplicateFlag += 1
                        res.append(task +'_FAILED DUPLICATE_' + 'TOPUP')
            
            else:
                res.append(task +'_FAILED' + ' ' + invalidDateString)
        
        else:
            
            if validDateBoolean:
                res.append('RENEWAL_AMOUNT ' + str(renewalAmount))
            
            else:
                res.append('SUBSCRIPTIONS_NOT_FOUND')
    
    if duplicateFlag:
        return [' '.join(x) for _, x in sorted(zip(arrangeResByKey, [i.split() for i in res]))]
    else:
        return res