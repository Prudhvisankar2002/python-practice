for r in range(1,4):
    for c in range(1,5):
        print(r,end='\t')
    print()





for r in range(1,4):
    for c in range(1,5):
        print(c-r,end='\t')
    print()




k=1
for r in range(1,4):
    for c in range(1,5):
        print(k,end='\t')
        k+=1
    print()




k='*'
for r in range(1,4):
    for c in range(1,5):
        print(k,end='\t')
    print()




for r in range(1,6):
    for c in range(1,5):
        if r%2==0:
            print('*',end='\t')
        else:
            print('$',end='\t')
    print()

for r in range(1,6):
    for c in range(1,5):
        if r%5==0:
            print('@',end='\t')
        elif r%2==0:
            print('$',end='\t')
        else:
            print('*',end='\t')
    print()



for r in range(1,6):
    for c in range(1,6):
        if c%2!=0:
            print('*',end='\t')
        else:
            print('$',end='\t')
    print()



k=64
for r in range(1,6):
    for c in range(1,5):
       print(chr(k+c),end='\t')
    print()




for r in range(1,6):
    for c in range(1,r+1):
        print(c,end='\t')
    print()



for r in range(1,6):
    for c in range(1,r+1):
        print('*',end='\t')
    print()



k=64
for r in range(1,6):
    for c in range(1,r+1):
        print(chr(k+c),end='\t')
    print()



for r in range(1,6):
    for c in range(1,r+1):
        print(r,end='\t')
    print()
































