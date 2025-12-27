import random
points=0
while True:
    a=random.randint(1,20)
    b=random.randint(1,10)
    print('your random number is:', a, b)
    result=eval(input('enter your correct answer: '))
    if result==a*b:
       print(result,'is a Correct answer')
       points+=10+points
       print('____________________________________')
       print('your winning points is :', points)
       print('____________________________________')
    else:
       print(result,'sorry..... wrong answer')
       break
print('____________________________________')
print('FINALLY YOU WINNING POINTS IS:', points)
print('____________________________________')
if points>=70:
    print('\t''SUPER...FANSTATIC...')
elif points>=50:
    print('\t''VERY..GOOD...')
elif points>=40:
    print('\t''IMPROVE...YOURSELF...')
else:
    print('\t''BETTER TO JOIN IN SCHOOL....')


