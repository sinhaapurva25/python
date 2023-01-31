import get_calculations

def result(lines):
    installments = dict()
    amounts = dict()
    payment_array = dict()
    res = []
    for i in lines:
        line = i.split()
        key = line[1]+'-'+line[2]
        
        if line[0] == 'LOAN':
            amounts[key] = get_calculations.amounts(int(line[3]),int(line[4]),int(line[5]))
            installments[key] = get_calculations.installments(amounts[key],int(line[4]))
        
        if line[0] == 'PAYMENT':
            payment_array[key] = list(map(int,line[3:]))
        
        if line[0] == 'BALANCE':
            amount_paid, remaining_emis = get_calculations.amount_paid_and_remaining_emis(int(line[3]), installments[key], key, payment_array, amounts)
            res.append(' '.join([line[1],line[2],str(int(amount_paid)),str(remaining_emis)]))
    
    return res