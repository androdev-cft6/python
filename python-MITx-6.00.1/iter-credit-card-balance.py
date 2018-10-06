# -*- coding: utf-8 -*-
def paymentCalculator(bal, rate, minrate):
    """
    bal - initial CC balance, float
    rate - yearly interest rate, float
    minrate - min monthly rate of bal , float
    
    returns cr card balance after making min monthly
    payments for a year
    """
    monBalance=bal
    monIntRate=rate/12
    
    
    
    
    for i in range(1,13):
        minPayment=monBalance*minrate
        unpaidBal=monBalance-minPayment
        monInterest=unpaidBal*monIntRate
        monBalance= unpaidBal +  monInterest
        print("Month " + str(i) + " remaining balance: " +
              str(round(monBalance, 2)))
            
    return monBalance
        
    
   
    
    
paymentCalculator(484, 0.2, 0.04)