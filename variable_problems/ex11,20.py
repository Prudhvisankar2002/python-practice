from email.charset import add_alias

depositamount=50000 #11
intrest=7.8
time=5
smipleintrest=(depositamount*intrest*time)/100
totalamount=(depositamount+smipleintrest)
print("deposit amount is:",depositamount)
print("simple intrest is:",smipleintrest)
print("total is:",totalamount)


a=2      #12
b=3
c=a
a=b
b=c
print("a is:",a)
print("b is:",b)


a=5       #13
b=7
print("a is:",b)
print("b is:",a)


a=9          #14
b=6
a=a*b
b=a//b
a=a//b
print(a)
print(b)

startreading=11236         #15
endreading=11494
kilometers=endreading-startreading
print("she travelling kilometers is:",kilometers)


manchuriya=220             #16
briyani=360
tip=20
manchuriyabill=(manchuriya*3)
briyaniabill=(briyani*2)
totalamount=(manchuriyabill+briyaniabill+tip)
totalpersons=3
sharingamount=(totalamount/totalpersons)
print("manchuriya amount is:",manchuriyabill)
print("briyani amount is:",briyaniabill)
print("add tip amount is:",tip)
print("Each person sharing amount is:",sharingamount)


milkbill=930.0                     #17
eachdaybill=(milkbill/31)
leavedaybill=(eachdaybill*4)
marchmonthbill=(milkbill-leavedaybill)
print("milk bill is:",milkbill)
print("each day bill is:",eachdaybill)
print("leave day bill is:",-leavedaybill)
print("march month bill is:",marchmonthbill)


attendeddays=94                          #18
totaldays=126
attendedpercentage=(attendeddays*100/totaldays)
print(attendedpercentage)
print("attendeddays is:",attendeddays)
print("total days is:",totaldays)
print("Attendece percetage is:",attendedpercentage)


watertin=20                        #19
perday=6
onedaycost=(watertin * perday)
augustmonthbill=(watertin*perday*31)
print("cost of water tin is:",watertin)
print("perday using water tins is:",perday)
print("one day cost for water tin is:",onedaycost)
print(" total august month bill is:",augustmonthbill)


petrolcost=108.96                            #20
totalamount=300
eachleterpertrol=(totalamount / petrolcost)
print("petrol cost is:",petrolcost)
print("avialable amount is:",totalamount)
print("avaialable petrol leters is:",eachleterpertrol)