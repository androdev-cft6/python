# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def minMoPayment(bal, rate):
    """
    bal - initial CC balance, float
    rate - yearly interest rate, float
        
    returns min monthly payment (multiple of $10 
    and the same for each month), to pay balance 
    within 12 month. at the end the bal could be negative
    """
    monBalance=0
    monIntRate=rate/12
    
    def roundToTen(num):
        return 10-num%10+num
    
    monPayment=roundToTen(int(bal/12))
    
    
    while monBalance>=0: 
        monBalance=bal
        for i in range(1,13):
            unpaidBal=monBalance-monPayment
            monInterest=unpaidBal*monIntRate
            monBalance= unpaidBal +  monInterest
            print("Month " + str(i) + " remaining balance: " +
                  str(round(monBalance, 2)))
        if monBalance>0:monPayment+=10    # adding $10 if bal
        print(monPayment)
            
    return monPayment
        
    
   
    
    
print("Lowest Payment: " + str(minMoPayment(3926,0.2)))