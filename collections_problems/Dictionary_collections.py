# // read multiple items from customer then find the bill amount?
d={}
ch='y'
sum=0
while ch=='y':
      pid=int(input('enter the pid: '))
      cost=float(input('enter the cost: '))
      d[pid]=cost
      ch=input('Do u want to continue? (y/n): ')
      sum=sum+cost
print(d)
print('total bill amount is:',sum)
#
#
#
# // read emp id then remove that record?
d1={11:'prudhvi',22:'sankar',33:'vishnu',44:'rama',55:'krishna'}
ch='y'
while ch=='y':
      nameid=int(input('enter your remove name id:'))
      if nameid in d1:
          print('enter name id i available')
          d1.pop(nameid)
          ch=input('Do u want remove any another id ? (y/n): ')
print(d1)
#
#
#
# //read employee name then print empid if read employee id print empname?
d2={101:'prudhvi',102:'sankar',103:'ramana',104:'lucky',105:'krishna'}
name=input('enter the name : ')
for i,j in d2.items():
         if d2[i]==name:
             print(i)
         else:
             print(name,'sorry.. this name not available in list')


