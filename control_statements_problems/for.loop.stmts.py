a=[5,9,6,2,7]
sum=0
for i in a:
    if i%2==0:
        sum=sum+i
print('sum of all even numbers is: ',sum)

a=[5,9,6,2,7]
sum=0
for i in a:
    if i%2!=0:
        sum+=i
print('sum of all odd numbers:',sum)



a=[5,9,6,2,7]
count=0
for i in a:
    if i%2==0:
        count+=1
print('total count of the even number is :',count)



a=[5,9,6,2,7]
evencount=0
oddcount=0
for i in a:
    if i%2==0:
        evencount+=1
    if i%2!=0:
        oddcount+=1
print('total even numbers:',evencount)
print('total odd numbers:',oddcount)



a=[5,9,6,2,7]
big=a[0]
for i in a:
    if i>big:
        big=i
print('biggest number is :',big)



a=[5,9,6,2,7]
small=a[0]
for i in a:
    if i<small:
        small=i
print('smallest number is :',small)



a=[5,9,6,7,27,20,25,11,15]
big=a[0]
small=a[0]
for i in a:
    if i>big:
        big=i
    if i<small:
        small=i
    difference=big-small
print('the difference is: ',difference)


a=[5,9,6,7,27,20,25,11,15]
num=int(input('enter the any number : '))
if num in a:
   print(num,'available')
else:
    print(num,'not available')



a=[5,9,6,2,3,7,8,9,7]
num=int(input('enter any number: '))
count=0
if num in a:
    count=a.count(num)
    print(num,'available',count,'times')
else:
    count=0
    print(num,' not available',count,'times')













