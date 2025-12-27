def calfinalbill(billamt,discountamt):
    finalbill=billamt-discountamt
    return finalbill
billamt=float(input("enter bill amount is:"))
discountamt=int(input("enter discount amount is:"))
finalbill=calfinalbill(billamt,discountamt)
print("final bill is:",finalbill)

