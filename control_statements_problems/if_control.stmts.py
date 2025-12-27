first=int(input('enter the first number is:'))               #1
second=int(input('enter the second number is:'))
if first>second:
    print('the biggest number is:',first)
elif first<second:
      print('the biggest number is:',second)
else:
    print('both are equal numbers')



usrname=input('enter your name:')                            #2
password=input('enter your password:')
if usrname=="venkat" and password=="sathya":
    print("vaild user")
else:
    print("invalid user")


amount=6000                                                 #3
withdraw=float(input("Enter the amount you want to withdraw: "))
if withdraw <=amount:
    print('your transaction was successful')
    balance=amount-withdraw
    print('updated balance is',balance)
else:
    print('sorry...! you have less amount')


temperature= float(input("Enter the temperature is: "))                  #4
if temperature > 35:
    print("Hot Day")
else:
    print("Normal Day")


year = int(input("Enter the birth year is: "))                           #5
age = 2025-year
if age>=18:
    print('your age is :',age)
    print("Adult")
else:
    print("Minor")


num = int(input("Enter the number is : "))                                #6
if num%3==0 and num %5==0:
    print("Number is divisible by both 3 and 5")
else:
    print("Not divisible by both numbers")


distance=float(input("Enter distance in kilometers is: "))               #7
if distance<=10:
   cost=distance*10
   print('your distance cost amount is:',cost)
elif distance>=10:
     cost=distance*8
     print('your distance cost amount is:',cost)



year = int(input("Enter the year is: "))                                #8
if (year%4==0 and year%100):
    print("Leap Year")
else:
    print("Not a Leap Year")


marks = float(input("Enter subject marks is: "))                       #9
if marks<0 or marks>100:
    print("Invalid Marks")



cost = float(input("Enter product cost: "))                          #10
qty = int(input("Enter quantity: "))
bill_amount = cost * qty
if bill_amount>=5000:
    discount=20
    discountamt= bill_amount*discount/100
    final_bill = bill_amount-discountamt
    print("Bill Amount:", bill_amount)
    print("Discount (20%):", discountamt)
    print("Final Bill:", final_bill)
else:
    print("Bill Amount:",bill_amount)
    print("No Discount")



annual_salary = float(input("Enter annual salary: "))               #11
monthly_salary = annual_salary/12
if monthly_salary>=50000:
    print("before monthly salary is:",monthly_salary)
    tax = monthly_salary * 12 / 100
    print("tax amount is:",tax)
    finalamt=monthly_salary+tax
    print('Monthly Salary and tax amount is:',finalamt)
else:
    tax = 0
    print("Monthly Salary:", monthly_salary)
    print("Tax:", tax)


productcost = float(input("Enter product cost:"))                        #12
qty = int(input("Enter quantity:"))
card = input("Do you have ICICI card?:")
billamt=productcost*qty
if card=="yes":
    discount = 15
    discountamt= billamt*15/100
    print('discount is:', discountamt)
    final_bill = billamt-discountamt
    print('final bill is:', final_bill)
elif card=="no":
    discount = 0
    final_bill = billamt
    print("Bill Amount:", billamt)
    print("Discount:", discount)
    print("Final Bill:", final_bill)



ticket_cost = float(input("Enter ticket cost: "))                   #13
tickets = int(input("Enter number of tickets: "))
bill_amount = ticket_cost * tickets
code = input("Enter coupon code: ")
if code =="SAVE20":
    count=20
    print('total ticket bill amount is:', bill_amount)
    discountamt= bill_amount*disdiscount/100
    print('discount aount is:', discountamt)
    final_bill = bill_amount - discount
    print('final bill is:', final_bill)
else:
    discount = 0
    final_bill = bill_amount
    print("Bill Amount:", bill_amount)
    print("Discount:", discount)
    print("Final Bill:", final_bill)



age = int(input("Enter age is: "))                                      #14
if age>=18 and age<=25:
    print("You are eligible to apply for this job")
else:
    print("Sorry...! yur eligible for jobAge")



a =float(input("Enter first number:"))                        #15
b =float(input("Enter second number:"))
c =float(input("Enter third number:"))
if a>=b and a>=c:
    print("A-Biggest number is :", a)
elif b>=a and b>=c:
    print("b-Biggest number is:", b)
else:
    print("c-Biggest number is:", c)





