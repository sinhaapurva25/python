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