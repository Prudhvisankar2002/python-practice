order=[]
print('//WELCOME TO DOMINOS PIZZA HUT//')
print('1.pizza')
print('2.breadsticks')
print('3.pasta')
print('4.burger')
print('5.cake')
print('6.chips')
ch='y'
while ch==('y'):
        choice=int(input('enter your choice:'))
        if choice>=1 and choice<=6:
            if choice==1:
                order.append('pizza')
            elif choice==2:
                order.append('breadsticks')
            elif choice==3:
                order.append('pasta')
            elif choice==4:
                order.append('burger')
            elif choice==5:
                order.append('cake')
            else:
                order.append('chips')
            ch = input('Do you want any item (y/n):')
        else:
            print('//enter in valid choice//')
print('your order is:',order)
ch1=input('DO you want modify order (y/n): ')
if ch1=='y':
   print('1.add item')
   print('2.delete item')
   print('3.modify item')
   choice=int(input('enter your add modify choice:'))
   if choice>=1 and choice<=3:
       if choice==1:
           print('1.pizza')
           print('2.breadsticks')
           print('3.pasta')
           print('4.burger')
           print('5.cake')
           print('6.chips')
           while ch1=='y':
               item=int(input('enter your choice:'))
               if item >= 1 and item <= 6:
                   if item == 1:
                       order.append('pizza')
                   elif item == 2:
                       order.append('breadsticks')
                   elif item == 3:
                       order.append('pasta')
                   elif item == 4:
                       order.append('burger')
                   elif item == 5:
                       order.append('cake')
                   else:
                       order.append('chips')
               else:
                   print('//enter in valid modifying choice//')
               ch1=input('Do you want any item (y/n):')
               print('your order is:',order)
       elif choice==2:
           ch2='y'
           while ch2=='y':
               print(order)
               remove=input('enter remove item name: ')
               if remove in order:
                   print(remove,'available ')
                   order.remove(remove)
                   ch2=input('Do you want remove any another item (y/n):')
                   print('your order is:',order)
               else:
                   print('//sorry..item is not available in your order//')
       else:
           ch3=('y')
           while ch3=='y':
               print(order)
               modify=input('enter your modify item name: ')
               if modify in order:
                   i=order.index(modify)
                   replace=input('enter replace item name: ')
                   order[i]=replace
                   print('your order is:',order)
   else:
       print('// invalid modifying choice// ')
else:
    print('//enter in valid choice//')
