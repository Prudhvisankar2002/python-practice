#w.a.p.read a multiple values from user then find sum.
sum=0
ch='y'
while ch=='y':
      n=int(input('enter the any number: '))
      sum+=n
      ch=input('Do you want continue (y/n):')
print('The sum of the numbers is',sum)



#w.a.p.read a multiple values from user then find sum of the even numbers only.
sum=0
ch='y'
while ch=='y':
      n=int(input('enter the any number: '))
      if n%2==0:
          sum+=n
      ch=input('Do you want continue (y/n):')
print('The sum of the numbers is',sum)


#w.a.p. read a number then print the sum as given number.
n=int(input('enter the any nuber: '))
sum=0
while n>0:
    r=n%10
    n=n//10
    sum+=r
print('the sum of the numbers is',sum)

#w.a.p. read a number then print the sum as given number.
n=int(input('enter the any nuber: '))
rev=0
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
print('the sum of the numbers is',rev)



n=int(input('enter the any number: '))
temp=n
reverse=0
while n>0:
    r=n%10
    reverse=reverse*10+r
    n = n // 10
print(reverse)
if temp==reverse:
    print('it is a palindrome')
else:
    print('it is not a palindrome')


evensum=0
n = int(input('enter the any number: '))
while n>0:
    r=n%10
    n=n//10
    if n%2==0:
        evensum+=r
print('sum of the even numbers:',evensum)




n = int(input('enter the any number: '))
evensum,oddsum=0,0
while n>0:
    r=n%10
    n=n//10
    if r%2==0:
        evensum+=r
    elif r%2!=0:
        oddsum+=r
print('sum of the even numbers:',evensum)
print('sum of the odd numbers:',oddsum)


n=int(input('enter the any number: '))
temp=n
count=0
while n>0:
    r=n%10
    n=n//10
    count+=1
print('enter value is:',temp)
print('count of digits:',count)



n=int(input('enter the any number: '))
temp=n
evencount=oddcount=0
while n>0:
    r=n%10
    n=n//10
    if r%2==0:
        evencount+=1
    else:
        oddcount+=1
print('total count of even count digits: ',evencount)
print('total count of odd count digits: ',oddcount)



n=int(input('enter the any number: '))
temp=n
sum=0
rev=0
n=n//10
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
print(rev)
rev=rev//10
print(rev)
while rev > 0:
    r=rev % 10
    rev=rev//10
    sum=sum+r
print('sum of all digits Expect first and last no: ',sum)



print('1.idly')
print('2.dosa')
print('3.puri')
print('4.vada')
discount=30
finalbill=0
ch='y'
while ch=='y':
        choice = int(input('enter the choice is: '))
        if choice>=1 and choice<=4:
            if choice==1:
                item='idly'
                cost=200
            elif choice==2:
                item='dosa'
                cost=300
            elif choice==3:
                item='puri'
                cost=400
            elif choice==4:
                item='vada'
                cost=500
            print('item',item,'cost=',cost)
            qty=int(input('enter the quantity is: '))
            billamt=cost*qty
            print('bill amount is:',billamt)
            ch=input('Do you want another (y/n): ')
            finalbill=finalbill+billamt
            print('final bill amount is : ',finalbill)
        else:
            print('enter valid choice')
if finalbill >= 1500:
    discountamt = finalbill * discount / 100
    print('discount percentage is % : ', discount,'%')
    print('discount amount is : ', discountamt)
    finalbillamt = finalbill - discountamt
    print('final bill is : ', finalbillamt)
    paid = float(input('enter the paid amount is :'))
    print('paid amount is : ', paid)
    balance = paid - finalbillamt
    print('Return balance amount is : ', balance)
else:
    d = 0
    damt = 0
    print('discount amount is : ', d)
    print('discount amount is : ', damt)
    print('final bill amount is : ', finalbill)
    paid = float(input('enter the paid amount is :'))
    print('paid amount is : ', paid)
    balance = paid - finalbill
    print('Return balance amount is : ', balance)





































