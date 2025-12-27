def calintrestamt(amount,time,intrest):
    intrestamt=amount*intrest*time/100
    return intrestamt
def calfinalamount(amount,intrestamt):
    finalamount=amount+intrestamt
    return finalamount
def calemi(finalamount,time):
    emi=finalamount/time*12
    return emi
amount=float(input("enter the loan amount is:"))
intrest=float(input("enter interest is:"))
time=float(input("enter time is:"))
intrestamt=calintrestamt(amount,time,intrest)
print("intrest amount is:",intrestamt)
finalamount=calfinalamount(amount,intrestamt)
print("final amount is:",finalamount)
emi=calemi(finalamount,time)
print("Your monthiy emi is:",emi)