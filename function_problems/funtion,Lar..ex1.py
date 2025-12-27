def caltotal(s1,s2,s3):
    total=s1+ s2+s3
    return total
s1=float(input("enter subject1 marks  is:"))
s2=float(input("enter subject2 marks is:"))
s3=float(input("enter subject3 markst is:"))
total=caltotal(s1,s2,s3)
print("total subject marks is:",total)
def calaverage(total):
    average=total/3
    return average
print("average percentage  is:",calaverage(total))