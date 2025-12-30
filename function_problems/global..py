amount=5000
def  deposit():
     global amount
     damount=2000
     print('enter deposit amount is:',damount)
     amount=amount+damount
def  withdraw():
     global amount
     wamount=5000
     print('enter withdraw amount is:',wamount)
     amount=amount-wamount
     print('blance amount is:',amount)
def  balance():
    global amount
    print('enter balance amount is:',amount)
deposit()
withdraw()
balance()


a=20
def show():
    global a
    a=a+30
    print(a)
b=30
def display():
    global b
    print(b)
show()
display()
