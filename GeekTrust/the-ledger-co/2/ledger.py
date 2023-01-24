import math

def Amounts(principal,numberOfYears,rateOfInterest):
    rateOfInterest /= 100
    interest = principal * numberOfYears * (rateOfInterest)
    amount = principal + interest

    return amount

def Installments(amount,numberOfYears):

    numberOfMonthsInAnYear = 12
    totalEmis = numberOfMonthsInAnYear * numberOfYears

    installment = list()
    # installment.extend([int(amount//totalEmis)+1 for i in range(int(amount%totalEmis))])
    # installment.extend([int(amount//totalEmis) for i in range(int(amount%totalEmis),int(totalEmis))])

    if amount%totalEmis == 0:
        installment.extend([int(amount//totalEmis) for i in range(int(totalEmis))])
    else:
        installment.extend([int(amount/totalEmis)+1 for i in range(int(totalEmis))])

    return installment

def amountPaidAndRemainingEmis(emiNumber, ins, key, paymentArray, amounts):
    amountPaid = sum(ins[:emiNumber])
    
    if key in paymentArray:
        payment = paymentArray[key]
        lumpSum = payment[0]
        emiNumberOflumpSum = payment[1]

        if emiNumberOflumpSum <= emiNumber:
            amountPaid += lumpSum    
    if amountPaid > amounts[key]:
        amountPaid = amounts[key]
    remainingEmis = math.ceil((amounts[key]-amountPaid)/ins[0])

    return amountPaid, remainingEmis


class loan():
    pass
class payment():
    pass
class balance():
    pass

def Result(Lines):
    installments = dict()
    amounts = dict()
    paymentArray = dict()
    res = []
    for i in Lines:
        line = i.split()
        key = line[1]+'-'+line[2]
        
        if line[0] == 'LOAN':
            amounts[key] = Amounts(int(line[3]),int(line[4]),int(line[5]))
            installments[key] = Installments(amounts[key],int(line[4]))
        
        if line[0] == 'PAYMENT':
            paymentArray[key] = list(map(int,line[3:]))
        
        if line[0] == 'BALANCE':
            amountPaid, remainingEmis = amountPaidAndRemainingEmis(int(line[3]), installments[key], key, paymentArray, amounts)
            res.append(' '.join([line[1],line[2],str(int(amountPaid)),str(remainingEmis)]))
    
    return res