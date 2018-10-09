# -*- coding: utf-8 -*-
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
    monthlyIntRate=rate/12
    minMonthlyPayment=round((int(bal/12)),3)
    maxMonthlyPayment=round((bal*(1+monthlyIntRate)**12)/12,3)
    monthlyPayment=0
    unpaidBal=1
    whileCounter=1
    
    while unpaidBal>0:  
        unpaidBal=bal               
        monthlyPayment=round((maxMonthlyPayment+minMonthlyPayment)/2,3) #bi-sectional search                  
        
        for i in range(1,13):       # look for 12 months                 
            unpaidBal -= monthlyPayment
            if unpaidBal>0:
                monInterest = unpaidBal*monthlyIntRate
            else:
                monInterest=0     
                maxMonthlyPayment=monthlyPayment
                break
            unpaidBal = unpaidBal + monInterest
                               
        unpaidBal=round(unpaidBal,2)        
        
        if unpaidBal>0: #shift search boundaries
            minMonthlyPayment=monthlyPayment  
        else:
            maxMonthlyPayment=monthlyPayment
            unpaidBal=bal
        
        if abs(unpaidBal)<=0.01:
            break
        
        whileCounter+=1  
        print("While Loop No: " + str(whileCounter))           
                                
    return monthlyPayment
        
    
   
a1=320000; i1=0.2
a2=999999; i2=0.18    
    
print("Lowest Payment 1: " + str(round(minMoPayment(a2, i2),2)))