def caldisamt(billamt,discount):
    disamt=billamt*discount/100
    return disamt
billamt=float(input("enter bill amount is:"))
discount=int(input("enter discount is:"))
print("discount  amount is:",caldisamt(billamt,discount))
