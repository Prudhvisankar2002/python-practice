def calfinallamount(loanamt,intrestamt):
    finallamount=loanamt+intrestamt
    return finallamount
loanamt=float(input("enter loan amount is:"))
intrestamt=float(input("enter intrest amount is:"))
finallamount=calfinallamount(loanamt,intrestamt)
print("final amount is:",finallamount)