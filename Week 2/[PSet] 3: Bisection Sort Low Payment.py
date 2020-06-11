bb = 999999
aRate = .18

def low(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12
    low = balance / 12
    high = (balance * (1+monthlyInterestRate)**12) /12.0
    step = .01
    monthly = (high+low)/2
    debt = balance
    while debt > 0 :
        debt = balance
        for i in range(12):
            debt -= monthly
            if debt <= 0:
                return monthly
            debt *= (monthlyInterestRate + 1) 
        if monthly < debt:
            low = monthly
        else:
            high = monthly
        
        monthly = (high+low)/2

    

print("Lowest payment: " + str(round(low(bb, aRate))),2)
