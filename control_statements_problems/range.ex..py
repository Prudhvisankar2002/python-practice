n=int(input('enter any number :'))
for i in range(1,n+1):
    if i%2==0:
        print(i)
print('even numbers:',i)



n=int(input('enter any number:'))
for i in range(n,1,-1):
    print(i)



n=int(input('enter  any number:'))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print('even numbers:',sum)



n=int(input('enter the any number:'))
product=1
for i in range(1,n+1):
    product*=i
print('product is=',product)



n=int(input('entered the any number:'))
for i in range(1,n+1):
    if i%5==0:
        print(i)



n=int(input('enter the any  number :'))
print('odd\teven')
for i in range(1,n+1,):
    if i%2==0:
        print(i)
    else:
        print(i,end="\t ")





startno=int(input('enter the any number:'))
endno=int(input('enter the any number:'))
step=0
for i in range(startno,endno):
     if startno>endno:
         step=-1
         endno=endno-1
     else:
         step=1
         endno=endno+1
     print(i,end='\t')











