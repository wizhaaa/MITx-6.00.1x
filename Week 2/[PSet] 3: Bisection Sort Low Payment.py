#bisection select
#expect 29157.09

balance = 320000
annualInterestRate = .2

def low(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12
    low = round(balance / 12 , 2 ) 
    high = round((balance * (1+monthlyInterestRate)**12) /12.0 , 2 )
    
    payment = round((high+low)/2,2)
    print('high is: ' + str(high))
    print('low is', str(low))
    print('initial monthly payment is ' , str(payment))

    debt = balance

    while low < (high - .001):
        payment = round((high+low)/2.0 ,2)
        debt = balance
        for i in range(12):
            debt -= payment
            debt *= (monthlyInterestRate + 1) 
        print('with a monthly payment of: ' + payment + ' we will pay: ' + str(payment*12))
        debt = balance
        if debt <= 0:
            low = payment
        else:
            high = payment    
        payment = (high+low)/2.0 

    print('this run:', str(payment))
    return payment


print("Lowest payment: " + str(round(low(balance, annualInterestRate),2)))
