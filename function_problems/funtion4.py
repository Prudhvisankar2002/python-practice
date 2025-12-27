def calattendecepercentage(worksdays,presentdays):
    calattendecepercentage=presentdays/worksdays*100
    return calattendecepercentage
worksdays=float(input("enter works days is:"))
presentdays=float(input("enter present days is:"))
attendecepercentage=calattendecepercentage(worksdays,presentdays)
print("attendece percentage is:",attendecepercentage)

