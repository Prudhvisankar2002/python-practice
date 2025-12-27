def calemi(totalamt,time):
    emi=totalamt/time*12
    return emi
totalamt=float(input("enter total amount is:"))
time=float(input("enter time is:"))
emi=calemi(totalamt,time)
print("monthly emi  is:",emi)
