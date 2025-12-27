s1=int(input('enter the sub-1 marks is:'))                 #1
s2=int(input('enter the sub-2 marks is:'))
s3=int(input('enter the sub-3 marks is:'))
total=s1+s2+s3
avg=total/3
if s1>=35 and s2>=35 and s3>=35:
    print('PASS')
    print('total marks is',total)
    print('average marks is',avg)
    if avg>=90:
        print("grade-A")
    elif avg>=80:
        print("grade-B")
    elif avg>=70:
        print("grade-C")
    else:
        print("grade-D")
else:
    print('FAIL')
    print(" BETTER LUCK NEXT TIME")




amount=5000                                                 #2
pin=int(input('Enter the your pin:'))
if pin==1122:
    wamt = float(input('enter the withdraw amount: '))
    if wamt<=5000:
        balance = amount-wamt
        print('withdraw amount is:',wamt)
        print('updated balance amount is:',balance)
    else:
        print('LESS AMOUNT HAVE IN YOUR ACCOUNT')
else:
    print('INVALID PIN')



n=int(input('enter the number is:'))                          #3
if n>=1 and n<=3:
    if n==1:
        print('one')
    elif n==2:
        print('two')
    else:
        print('three')
else:
    print('invalid number')



unit=int(input("Enter the units: "))                            #4
if unit<100:
    bill=unit*1.5
    print('the total bill amount is:',bill)
elif unit<200:
    bill=unit*2.5
    print('the total bill amount is:',bill)
elif unit<300:
    bill=unit*4
    print('the total bill amount is:',bill)
else:
    bill=unit*6
    print('the total bill amount is:',bill)



temperature=int(input("enter temperature is: "))                     #5
if temperature>30:
    print('It too hot, stay indoors')
elif temperature>25:
    print('nice weather, go outside')
elif temperature>15:
    print('cool weather, wear jacket')
else:
    print('Too cold,stay warm')



temperature=int(input("enter temperature is:"))                          #6
cough=input('enter you have cough (yes or no):')
tiredness=input("enter you have tiredness (yes or no):")
if temperature>99:
   print('you have fever ')
   if cough=='yes':
     print('you might have a cold ')
     if tiredness=='yes':
        print('take some rest')
else:
    print("Invalid Enter")




age = int(input("Enter your age is:"))                                #7
qualificatioon = input("Enter your qualification is:")
experience = int(input("Enter your experience is (years):"))
if age >= 18:
    print('age eligible')
if qualificatioon == "graduate":
    print('qualification is eligible')
if experience>=2:
    print('experience is eligible')

else :
    print ('not eligible for job')



income=float(input("Enter income amount is: "))                          #8
if income>=25000:
    creditscorce=int(input("Enter your credit score is: "))
    if creditscorce>=700:
        print('eligible for loan')
    else:
        print('you have a less credit score')
        print("sorry not eligible for loan")
else:
    print(" your Income is less than 25000")



age=int(input("Enter your age is:"))                                       #9
if age<=18:
   print(' Not eligible ')
elif age>60:
     print('senior citizen_medical check required')
elif age >= 18 and age <= 60:
     print('eligible for licence')
     vision = input("Enter your vision (good/bad):")
     test = input("Enter your test (passed/failed):")
     if vision == "good" and test == "passed":
        print('licence is approved')
     else:
         print('failed vision and test')




























