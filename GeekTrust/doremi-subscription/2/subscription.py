# defining global variables
noOfMonths = 12
noOfMonthsNextYr = 3
oddMonths = [1, 3, 5, 7, 8, 10, 12]
daysOddMonths = 31
evenMonths = [4, 6, 9, 11]
daysEvenMonths = 30
lpYrCondOne = 400
lpYrCondTwo = 100
lpYrCondThree = 4
daysLeapFeb = 29
daysNonLeapFeb = 28

price =    {'MUSIC FREE': 0,
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
    return ((yy % lpYrCondOne == 0) or (yy % lpYrCondTwo != 0) and (yy % lpYrCondThree == 0))


def appendZero(y):
    if y < 10:
        return '0' + str(y)
    else:
        return str(y)


def days(calendar, noOfDays, month, year):
    for dt in range(1, noOfDays+1):
        day = ""
        day += appendZero(dt)
        day += '-'
        day += appendZero(month)
        day += '-'
        day += str(year)
        calendar.append(day)
    return calendar


def months(calendar, daysArr, noOfMonths, yy):
    for i in range(1,noOfMonths+1):
        
        if i in oddMonths:
            noOfDays = daysOddMonths

        elif i in evenMonths:
            noOfDays = daysEvenMonths

        else:
            if leapYear(yy):
                noOfDays = daysLeapFeb
            else:
                noOfDays = daysNonLeapFeb
        
        days(calendar, noOfDays, i, yy)
        
        daysArr.append(noOfDays)
    return daysArr, calendar


def getCalendar(yy):
    daysArr = list()
    calendar = list()
    
    months(calendar, daysArr, noOfMonths, yy)
    
    yy += 1
    months(calendar, daysArr, noOfMonthsNextYr, yy)

    return daysArr, calendar


def validDate(dd, mm, yy):

    validDateBool = True

    if mm > noOfMonths:
        validDateBool = False
    else:
        if mm in oddMonths:
            if dd > daysOddMonths:
                validDateBool = False
        elif mm in evenMonths:
            if dd > daysEvenMonths:
                validDateBool = False
        else:
            if leapYear(yy):
                if dd > daysLeapFeb:
                    validDateBool = False
            else:
                if dd > daysNonLeapFeb:
                    validDateBool = False
    return validDateBool


def calculate(Lines):
    res = list()
    
    dateIndex = 1
    firstLineIndex = 0
    dd, mm, yy = list(map(int, Lines[firstLineIndex].split(" ")[dateIndex].split("-")))
    validDateBool = validDate(dd, mm, yy)
    
    invalidDateString = 'INVALID_DATE'
    if validDateBool:
        daysArr, calendar = getCalendar(yy)
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

            if validDateBool:

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
            
            if validDateBool:
                res.append('RENEWAL_AMOUNT ' + str(renewalAmount))
            
            else:
                res.append('SUBSCRIPTIONS_NOT_FOUND')
    
    if duplicateFlag:
        return [' '.join(x) for _, x in sorted(zip(arrangeResByKey, [i.split() for i in res]))]
    else:
        return res