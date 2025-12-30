#// w.a.p. to read pid,pname,cost, of the multiple elements then add to orders?
orders={}
ch='y'
while ch=='y':
    pid=int(input("enter pid:"))
    pname=input("enter name:")
    cost=float(input("enter cost:"))
    orders[pid]=[pname,cost]
    ch=input('do you want to continue?(y/n)')
print('your orders:',orders)


#//consider the customer orders={'idly':[50.0,3,150.0],'dosa':[100.0,3,300.0]} now find the fill formated?
                      # s.no       itemname        cost      qty         mount
                      #
                      #  1          idly           50.0      3          150.0
                      #  2          dosa           100.0     3           300.0

orders={}
sum=0
ch='y'
while ch=='y':
    pname=input("enter the name:")
    cost = float(input("enter the cost:"))
    qty=int(input("enter the qty:"))
    amount=cost*qty
    orders[pname]=[cost,qty,amount]
    ch=input('do you want to continue?(y/n)')
    sum = sum + amount
print('your order is:',orders)
for i,j in orders.items():
    print(i,'',end='\t')
    for k in j:
        print(k,'',end='\t')
    print()
sno=1
print('s.no \titem_name\tcost \tqty \tamount ')
for i,j in orders.items():
    print(sno,end='\t\t')
    sno+=1
    print(i,'',end='\t')
    for k in j:
        print(k,end='\t\t')
    print()
    print('__________________________________________')
print('\t\t total amount:',sum)
print('__________________________________________')

items={'dosa':50.0,'idly':90.0,'puri':100.0}
order={}
sum=0
print('welcome to MAA HOTEL')
print('1.dosa')
print('2.idly')
print('3.puri')
ch='y'
while ch=='y':
       choice=int(input('enter your choice: '))
       if choice>=1 and choice<=3:
           if choice==1:
               order['dosa']=items['dosa']
               cost=90
           elif choice==2:
               order['idly']=items['idly']
               cost=90.0
           else:
               order['puri']=items['puri']
               cost=100.0
           qty=int(input('enter your qty: '))
           amount=cost*qty
           ch = input('Do you want to continue? (y/n):')
           sum = sum + amount  
       else:
           print('invalid choice')
print('your order is:',order)
print('your sum is:',sum)


