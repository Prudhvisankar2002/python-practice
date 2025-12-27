# a=[5,9,3,12,5,7]
# n=int(input('enter any number: '))
# i=a.index(n)
# count=a.count(n)
# print(i)
# print(count)


# a=[5,9,3,12,5,7]
# b=a.copy()
# b[1]=20
# b=sorted(b)
# print(a)
# print(b)

# a=[]
# ch='y'
# while ch=='y':
#     n=int(input('enter number: '))
#     a.append(n)
#     ch=input('do want add element into list(y/n): ')
# print('your is is ',a)


a=[5,9,3,12,5,7]
ch='y'
while ch=='y':
      n=int(input('enter number: '))
      if n in a:
          i=a.index(n)
          m=int(input('enter new number: '))
          a[i]=m
          ch=input('do you want again number(y/n): ')
      else:
          print('the number is not in the list')
print('your list is:',a)
