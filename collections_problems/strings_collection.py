##//w.a.p.to read a string then print only vowels in your string?
# s=input('enter a string:')
# for i in s:
#     if i in 'aeiou':
#         print(i)


##//w.a.p.to read string then print all lower case letters?
# s=input('enter the any name: ')
# for i in s:
#     if i>='a' and i<='z':
#         print(i)


##//w.a.p.to read string then print the count of all lower case letters?
# s2=input('enter any string: ')
# count=0
# for i in s2:
#     if i>='a' and i<='z':
#         count+=1
# print(count)


##//w.a.p. to read a string then display the reverse string order?
# s=input('enter a string: ')
# s2=s[::-1]
# print('given string is',s)
# print(s2)



##//w.a.p.read a string then check the given string is palindrome are not?
# s=input('enter the any string: ')
# s1=s[::-1]
# if s==s1:
#     print(s,'is palindrome')
# else:
#     print(s,'is not palindrome')



##//w.a.p.to read string then print the count of all uppercase letters?
# s=input('enter any string: ')
# count=0
# for i in s:
#     if i>='A' and i<='Z':
#        count+=1
#        print(count)
#     else:
#         print('there is no uppercase letter')



##//w.a.p. to read password from user then count the no.of. lowercase,uppercase letters in string?
# s=input('enter any string: ')
# uppercount,lowercount=0
# for i in s:
#     if i>='A' and i<='Z':
#        uppercount+=1
#        print('uppercase letter count is : ',uppercount)
#     else:
#         lowercount+=1
#         print('lowercase letter count is : ',lowercount)


##//read password to check string maintain with 1-uppercase,1-lowercase,1-digit,1-symbol and above 8 to14 characters maintain?
# s=input('enter any password: ')
# upper=0
# lower=0
# symbol=0
# digit=0
# for i in s:
#     if len(i)>=8 and len(i)<=14:
#         if i>='A' and i<='Z':
#            upper+=1
#         elif i>='a' and i<='z':
#             lower+=1
#         elif i>='0' and i<='9':
#             digit+=1
#         else:
#             symbol+=1
# if lower > 0 and upper>0  and digit>0 and symbol>0:
#          print('valid password')
# else:
#          print('invalid password')



##//comparisions we have 3 opitions?
## 1) use'=='symbol is used to compare complete string ?
##2) use startswith():- method to compare starting of a string ?
## 3) use endswith() :- methode to compare with end of the string?

# pwd='venkat'
# s=input('enter any string:')
# if s==pwd:
#     print('enter the string valid ')
# else:
#     print('enter string is invalid string')


# code=eval(input('enter the code :'))
# ht='1122CSE001'
# if ht.startswith(code):
#     print('belongs to our college')
# else:
#     print('not belongs to our college')


# emailid='prudhvisankar@ibm.com'
# if emailid.endswith('ibm.com'):
#     print('belongs to ibm company')
# else:
#     print('not belongs to ibm company')




##//replace() :--> it si used to replace the existing character / string with new?
# s='core java and avd java both are imp for java'
# s1=s.replace('j','b')
# print(s1)


##//split() :--> it is used to divide given string into multiple parts based in the given character ,incase user doesn`t speify  any character
##             then it will split based on space.

# s='core java and avd java both are imp for java'
# s1=s.split()
# print(s1)
# #
# count=0
# for i in s1:
#     count+=+1
# print(count)
# #
# s1[5]='prudhvi'
# print(s1)
# #
# s1.remove('java')
# print(s1)


# s='prudhvi@2002'
# s1=s.split('@')
# print(s1)
# print('emp name is:',s1[0])


# s='PRUdhvisankAR'
# s1=s.islower()
# print(s1)


# s='PRUdhvisankAR'
# s1=s.lower()
# print(s1)
#
#
# s='PRUdhvisankAR'
# s1=s.upper()
# print(s1)



# s='   venkat    '
# print(len(s))
# s1=s.strip()
# print(len(s1))

# s='sathya technology'
# for i in s:
#     if i in 'aeiou':
#         print(i,end='\t')


## find hall_tickets number from given list to use code from user?
# ht=['112221001','115622053','112221022','185621050','112221029','115622023','116522001']
# code=input('Enter college code: ')
# result=[]
# for i in ht:
#     if i.startswith(code):
#         result.append(i)
# if result:
#     print('your hall_ticket numbers')
#     for h in result:
#         print(h)
# else:
#     print('sorry.. no hall_tickets available')


# s='sathya technology'
# result=""
# for i in s:
#     if i in 'aeiou' and i not in result:
#         result+=i
# print(result)
