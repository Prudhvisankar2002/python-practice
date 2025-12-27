# list functions they are:-
# sum()
# min()
# max()
# len()
# sorted()
# list()
#
#
# Group of character data :-
#  1.list   //group of elements values including duplicates and went do modifications//=>a[1,2,3,4,5]
#
#  2.tuple  //group of elements values including duplicates is NOTALLOWED MODIFICATIONS//a=('cse','IT')
#
#  3.set   //group of values including without duplicates then use set of modifications allowed//s={1,2,3,4,6}
#
#  4.dictionary  //used to store group of values in the form of key-value pairs // d={101:'vishnu', 102:'prudhvi'}
#
#  .strings :anything enclosed with single or double quotes is called string //s='prundhvi sankar'
#
# //  slicing problems:=

a=[1,7,5,4,2,6]

print(a[1:4])

print(a[::])

a.append(6)
a.append(9)
print(a)

a.remove(3)
print(a)


print(sum(a))
print(max(a))
print(min(a))
print(len(a))
print(sorted(a))


# //consider a=[5,6,3,9,2] now read elements then remove from your list?

a=[5,6,3,9,2]
n=int(input('enter the removing number: '))
if n in a:
    a.remove(n)
    print(a)
else:
    print('number is not available in the list')


#//consider a=[5,6,3,9,2]   now read  Number and modify it?

a=[5,6,3,9,2]
n=int(input('enter the modification number: '))
if n in a:
    i=a.index(n)
    m=int(input('enter the adding number: '))
    a[i]=m
    print(a)
else:
    print('number is not available in the list')


#// consider the order ['idly','vada','puri'] now modify?

order=['idly','vada','puri']
n=input("Enter the which item u want: ")
if  n in order:
    if n=='vada':
       print('vada is available in index 1')
       i=order.index(n)
       m=int(input("Enter which item u want  into list: "))
       order[i]=m
       print(order)
    elif n=='puri':
       print('puri is available in index 2')
       i=order.index(n)
       m=input("Enter which item u want into list: ")
       order[i]=m
       print(order)
    elif n=='idly':
       print('vada is available in index 0')
       i=order.index(n)
       m=input("Enter which item u want  into list: ")
       order[i]=m
       print(order)
else:
    print(n,'items not available in list')
    print(order)





order=['idly','vada','puri']
n=input('enter the modify item: ')
if n in order:
    if n=='idly':
        order.remove(n)
        print(n,'is deleted from order list')
        print(order)
    elif n=='vada':
        order.remove(n)
        print(n,'is deleted from order list')
        print(order)
    elif n=='puri':
        order.remove(n)
        print(n,'is deleted from order list')
        print(order)
else:
    print(n,'is not in the order list')
    print(order)




menu=[]
print('1.idly')
print('2.dosa')
print('3.vada')
print('4.puri')
ch='y'
while ch=='y':
      choice = int(input('enter a choice: '))
      if choice >= 1 and choice <= 4:
            if choice == 1:
                  menu.append('idly')
            elif choice == 2:
                  menu.append('dosa')
            elif choice == 3:
                  menu.append('vada')
            else:
                  menu.append('puri')
      else:
            print('enter a valid choice')
      ch = input('Do u want to continue? (y/n): ')
print(menu)


