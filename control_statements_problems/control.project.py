print("WELCOME TO KEKA HOTEL")
print('AVAILABLE ITEMS IN KEKA HOTEL IS :')
print('1.idly  -50.0')
print('2.dosa  -100.0')
print('3.vada  -150.0')
print('4.puri  -120.0')
discount=20
choice=int(input('enter the choice:'))
if choice>=1 and choice<=4:
    if choice==1:
        print('idly cost is : 50.0')
        cost=50
    elif choice==2:
        print('dosa cost is : 100')
        cost=100
    elif choice==3:
        print('vada cost is : 150')
        cost=150
    elif choice==4:
        print('puri cost is : 120')
        cost=120
    else:
        print('invalid choice')
    qty = int(input('enter the qty is:'))
    billamt = cost * qty
    print('total bill amount is : ', billamt)
    if billamt>=300:
       discountamt=billamt*discount/100
       print('discount percentage is % : ',discount)
       print('discount amount is : ',discountamt)
       finalbill=billamt-discountamt
       print('final bill is : ',finalbill)
       paid=float(input('enter the paid amount is :'))
       print('paid amount is : ',paid)
       balance=paid-finalbill
       print('Return balance amount is : ',balance)
    if billamt<=300:
        d=0
        damt=0
        print('discount amount is : ',d)
        print('discount amount is : ',damt)
        print('final bill amount is : ', billamt)
        paid=float(input('enter the paid amount is :'))
        print('paid amount is : ',paid)
        balance=paid-billamt
        print('Return balance amount is : ',balance)

else:
    print('SORRY.. NO MATCHING FOUND ')