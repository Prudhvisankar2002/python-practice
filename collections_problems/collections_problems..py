##// w.a p to read string the count no.of uppercase letters?
# ch=input('enter a string:')
# count=0
# for i in ch:
#     if i>='A' and i<='Z':
#         count+=1
#     else:
#         print('no uppercase are available in string')
# print(count)


##//w.a.p to read password from user then count no.of lowercase,uppercase,digits and symbols?
# password=input('enter the  password: ')
# lowercase=uppercase=digit=symbol=0
# for i in password:
#     if i>='a' and i<='z':
#         lowercase+=1
#     elif i>='A' and i<='Z':
#         uppercase+=1
#     elif i>='0' and i<='9':
#         digit+=1
#     else:
#         symbol+=1
# print('lowercase letters:',lowercase)
# print('uppercase letters:',uppercase)
# print('digits:',digit)
# print('symbols:',symbol)

##// w.a.p to read password from the user then check password id valid are invalid
##   ** if password length should be between 8-14 characters
##    ** password should be maintain:
##                                  ---> at least 1lowercase , 1 uppercase ,digit 1 ,symbol 1
password=input('Enter your password: ')
lowercase=uppercase=digit=symbol=0
for i in password:
     if len(i)>=8 and len(i):
        if i>='a' and i<='z':
             lowercase=lowercase+1
        elif i>='0' and i<='9':
            digit=digit+1
        elif i>='A' and i<='Z':
            uppercase = uppercase + 1
        else:
            symbol = symbol +1
else:
    print('inter invalid password')
