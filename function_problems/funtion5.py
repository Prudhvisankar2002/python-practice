def calintrestamount(amount,time,intrest):
    intrestamount=amount*time*intrest/100
    return intrestamount
amount=float(input("enter amount is:"))
time=float(input("enter time is:"))
intrest=float(input("enter intrest amount is:"))
intrestamount=calintrestamount(amount,time,time)
print("intrest amount is:",intrestamount)