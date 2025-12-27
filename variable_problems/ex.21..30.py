mangobasketcost=1150     #21
sellingprice=1680
profit=(sellingprice-mangobasketcost)
print("mango basket cost is:",mangobasketcost)
print("basket selling price is:",sellingprice)
print("mango basket profit is:",profit)


productcost=200                  #22
gst=20
gstamount=(productcost*gst)/100
finalcoat=productcost+gstamount
print("product cost is:",productcost)
print("gst amount is:",gstamount)
print("final coat amount is:",finalcoat)


pizzacost=326.50                     #23
qty=3
totalamount=(pizzacost*qty)
discountamount=(totalamount*20/100)
print("pizza cost is:",pizzacost)
print("qty is:",qty)
print("total amount is:",totalamount)
print("discount is:-",discountamount)
finalamount=(totalamount-discountamount)
print("final amount is:",finalamount)


salary=30000                #24
pf=12
tax=8
totaltax=pf+tax
taxamount=salary*totaltax/100
finalsalary=salary-taxamount
print("final salary is:",finalsalary)


loan=50000                       #25
intrest=11.4
time=4
intrestamount=loan*intrest*time/100
print("loan amount is:",loan)
print("rate of intrest is:",intrest)
print("year of time is:",time)
print("intrest amount is:",intrestamount)
finalamount=loan+intrestamount
print("final amount is:",finalamount)


lastmonthreading=2234                   #26
currentmonthreading=2456
perunittax=3.52
servicecharge=30
finalamount=(currentmonthreading-lastmonthreading)
totalbill=(finalamount*perunittax)+servicecharge
usingunits=finalamount*perunittax
print("final amount is:",finalamount)
print("using units is:",usingunits)
print("service charge is:",servicecharge)
print("total bill is:",totalbill)


startingreading=11236            #27
endingreading=11494
perkmcharge=50
totaltravelling=endingreading-startingreading
print("she total travelling is:",totaltravelling)
print("per km charge is:",perkmcharge)
kmcharge=(totaltravelling*50)
print("total km charge is:",kmcharge)
tollgatecharge=200
print("tollgate charge is:+",tollgatecharge)
finalbill=kmcharge+tollgatecharge
print("total travelling bill is:",finalbill)


emp_id=input("enter employee id:")          #28
emp_name=input("enter employee name:")
gender=input("enter gender(male,female,other):")
salaryamount=float(input("enter monthly salary amount:"))
annualsalary=salaryamount*12
print("annualsalary is:",annualsalary)


briyanicost=395.25              #29
print("briyani cost is:",briyanicost)
qty=int(input("enter how many qty:"))
totalbill=qty*briyanicost
print("total bill:",totalbill)


amount=float(input("enter rupees amount:"))            #30
dollaramount=(amount*83)
print("dollaramount:",dollaramount)