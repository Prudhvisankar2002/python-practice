def show(a,b,c,d):                #1
    tot=a+b
    return tot
tot=show(1,2,3,4)
print(tot)


def display():                    #2
    p=5
    q=7
    return p,q
a,b=display()
print(a,b)


def emical(b,t,r):                #3
    intrest=(b*t*r)/100
    return intrest
intamt=emical(100,2,2)
print(intamt)


def payment(cardno,name):          #4
    print(cardno)
    print(name)
    return True
res=payment(111,"sankar")
print(res)

def caltotal(a,b,c):               #5
    total=a+b+c
    return total
def calavg(t):
    avg=t/3
    return avg
tot=caltotal(1,2,3,)
average=calavg(30)
print(tot)
print(average)


amt=5000                           #6
def withdrawamt(wamt):
    print(amt)
    return amt
    print(wamt)
a=withdrawamt(3000)
print(a)


def calsquare(a):                   #7
    s=a*a
    return s
res=calsquare(2)
print(res)


def calavg(a,b,c):                   #8
    s=a+b+c
    return a,b,c
res=calavg(1,2,3)
print(res)


def show():                          #9
    print("hai")
    return 5
    print("helo")
a=show()


def display(a,b):                    #10
    a=9
    b=7
    c=a+b
    return c
p=display(3,9)
print(p)


def calbill(p,q):                      #11
    bill=p*q
    return bill
res=calbill(100,30)
print(res)


def intrest(p,t,r):                    #12
    iamt=p*t*r/100
    return iamt
amt=intrest(5000,2,55)
print(amt)
