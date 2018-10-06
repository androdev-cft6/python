# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def minMoPayment(bal, rate):
    """
    bal - initial CC balance, float
    rate - yearly interest rate, float
        
    returns min monthly payment (accurate to $0.01), to pay balance 
    within 12 month. at the end the bal could be negative
    
    Mo interest rate = (Annual interest rate) / 12.0
    Mo payment lower bound = Balance / 12
    Mo payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0
    """
    unpaidBal=bal
    monthlyIntRate=rate/12
    minMonthlyPayment=(int(bal/12))
    maxMonthlyPayment=(bal*(1+monthlyIntRate)**12)/12
    
    
    while unpaidBal>0: 
        monthlyPayment=(maxMonthlyPayment+minMonthlyPayment)/2 #bi-sectional search          
        
        for i in range(1,13):
            print("Using monthly payment of: " + str(monthlyPayment) + "\n")          
            unpaidBal -= monthlyPayment
            if unpaidBal<monthlyPayment:
                maxMonthlyPayment=monthlyPayment
                break
            monInterest = unpaidBal*monthlyIntRate
            unpaidBal += monInterest
            print("Month " + str(i) + " remaining balance: " +
                 str(round(unpaidBal, 2)))             
            
        if unpaidBal>0: #shift search boundaries
            minMonthlyPayment=monthlyPayment        
             
        
        unpaidBal=bal
                
    return monthlyPayment
        
    
   
    
    
print("Lowest Payment: " + str(minMoPayment(3926,0.2)))