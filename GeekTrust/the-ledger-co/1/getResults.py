import getCalculations

def Result(Lines):
    installments = dict()
    amounts = dict()
    paymentArray = dict()
    res = []
    for i in Lines:
        line = i.split()
        key = line[1]+'-'+line[2]
        
        if line[0] == 'LOAN':
            amounts[key] = getCalculations.Amounts(int(line[3]),int(line[4]),int(line[5]))
            installments[key] = getCalculations.Installments(amounts[key],int(line[4]))
        
        if line[0] == 'PAYMENT':
            paymentArray[key] = list(map(int,line[3:]))
        
        if line[0] == 'BALANCE':
            amountPaid, remainingEmis = getCalculations.amountPaidAndRemainingEmis(int(line[3]), installments[key], key, paymentArray, amounts)
            res.append(' '.join([line[1],line[2],str(int(amountPaid)),str(remainingEmis)]))
    
    return res