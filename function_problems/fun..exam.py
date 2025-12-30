def f1():
    print("core python")
f1()
print("bye")

def f2():
    print("hello")
def f1():
    f2()
    print("core python")
f1()
print('bye')

def f1():      #error
    print("core python")
    f2()
    print("venkat reddy")
f1()
print('byee')


def f1():
    print("core python")
    f2()
    print('vemkat reddy')
def f2():
    print("avdanced python")
f1()
print("byee")


def balenq():       #error
       print('you have balance')
def withdraw():
balenq()
    print('you have withdrawn')
balenq()
print('welcome to maa bank')
withdraw()


def search():     #error
    print('sreach ur iteam')
    print('select ur iteam')
    print('see ur review')
defbookitem():
    print('add to caart')
    print('click buy new opition')
def payment():
    print('pay amount')
print('welcome to amazon ')
search()
bookiteam()
payment()


def search():
    print('enetr the pincode ')
deforderiteam():
    search()
    print('give ur order')
orderiteam()
print("thank you")


def f1 ():
    print('hai')
    f2 ()
def f2 ():
    print("hello")
    f1 ()
f2 ()

