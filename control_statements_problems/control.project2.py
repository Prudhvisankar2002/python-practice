print('WELCOME TO KEKE HOTEL')
print('AVAILABLE ITEMS IN KEKE HOTEL IS:')
print('1.dosa')
print('2.vada')
print('3.idly')
choice=int(input("enter your choice:"))
discount=30
if choice>=1 and choice<=3:
    if choice==1:
       print('SELECT WHICH TYPE OF DOSA')
       print('1.plane dosa')
       print('2.onion dosa')
       print('3.masala dosa')
       print('4.egg dosa')
       print('5.double egg dosa')
       print('6.toppy dosa')
       type=int(input("enter your type of dosa: "))
       if type>=1 and type<=6:
           if type==1:
               print('plane dosa cost =100')
               cost=100
           elif type==2:
               print('onion dosa cost =150')
               cost=150
           elif type==3:
               print('masala dosa cost =200')
               cost=200
           elif type==4:
               print('egg dosa cost =250')
               cost=250
           elif type==5:
               print('double egg cost =300')
               cost=300
           elif type==6:
               print('toppy cost =350')
               cost=350
           qty = int(input('enter the qty is:'))
           billamt = cost * qty
           print('total bill amount is : ', billamt)
           if billamt >= 300:
               discountamt = billamt * discount / 100
               print('discount percentage is % : ', discount)
               print('discount amount is : ', discountamt)
               finalbill = billamt - discountamt
               print('final bill is : ', finalbill)
               paid = float(input('enter the paid amount is :'))
               print('paid amount is : ', paid)
               balance = paid - finalbill
               print('Return balance amount is : ', balance)
           if billamt <= 300:
               d = 0
               damt = 0
               print('discount amount is : ', d)
               print('discount amount is : ', damt)
               print('final bill amount is : ', billamt)
               paid = float(input('enter the paid amount is :'))
               print('paid amount is : ', paid)
               balance = paid - billamt
               print('Return balance amount is : ', balance)
       else:
           print('invalid type entered')
    elif choice==2:
       print('SELECT WHICH TYPE OF VADA')
       print('1.vada')
       print('2.sambar vada')
       print('3.masala dosa')
       print('4.onion vada')
       type = int(input("enter your type of vada: "))
       if type >= 1 and type <= 4:
           if type == 1:
              print('normal vada cost =100')
              cost = 100
           elif type == 2:
                print('sambar vada cost =150')
                cost = 150
           elif type == 3:
                print('masala vada cost =200')
                cost = 200
           else:
                print('onion vada cost =250')
                cost = 250
           qty = int(input('enter the qty is:'))
           billamt = cost * qty
           print('total bill amount is : ', billamt)
           if billamt >= 300:
               discountamt = billamt * discount / 100
               print('discount percentage is % : ', discount)
               print('discount amount is : ', discountamt)
               finalbill = billamt - discountamt
               print('final bill is : ', finalbill)
               paid = float(input('enter the paid amount is :'))
               print('paid amount is : ', paid)
               balance = paid - finalbill
               print('Return balance amount is : ', balance)
           if billamt <= 300:
               d = 0
               damt = 0
               print('discount amount is : ', d)
               print('discount amount is : ', damt)
               print('final bill amount is : ', billamt)
               paid = float(input('enter the paid amount is :'))
               print('paid amount is : ', paid)
               balance = paid - billamt
               print('Return balance amount is : ', balance)
       else:
         print('invalid.....type')
    elif choice==3:
       print('SELECT WHICH TYPE OF IDLY')
       print('1.normal idly')
       print('2.sambar idly')
       print('3.ghee idly')
       type = int(input("enter your type of idly: "))
       if type >= 1 and type <= 3:
           if type == 1:
              print('normal idly cost =100')
              cost = 100
           elif type == 2:
                print('sambar idly cost =150')
                cost = 150
           elif type == 3:
                print('ghee idly cost =200')
                cost = 200
           qty = int(input('enter the qty is:'))
           billamt = cost * qty
           print('total bill amount is : ', billamt)
           if billamt >= 300:
               discountamt = billamt * discount / 100
               print('discount percentage is % : ', discount)
               print('discount amount is : ', discountamt)
               finalbill = billamt - discountamt
               print('final bill is : ', finalbill)
               paid = float(input('enter the paid amount is :'))
               print('paid amount is : ', paid)
               balance = paid - finalbill
               print('Return balance amount is : ', balance)
           if billamt <= 300:
               d = 0
               damt = 0
               print('discount amount is : ', d)
               print('discount amount is : ', damt)
               print('final bill amount is : ', billamt)
               paid = float(input('enter the paid amount is :'))
               print('paid amount is : ', paid)
               balance = paid - billamt
               print('Return balance amount is : ', balance)
       else:
         print('invalid...option..check gain..')
else:
    print('INVALID .... PLEASE CHECK AGAIN ')

