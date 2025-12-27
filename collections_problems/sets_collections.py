j={'allen solly','wrangler','pepe jeans','levis','flying machine','allen solly','spykar','van veusen'}
b={'allen solly','mufti','wrangler','pepe jeans','lee','van heusen','monte carlo','flying machine'}

#//display the common brands available in two places?
j={'allen solly','wrangler','pepe jeans','levis','flying machine','allen solly','spykar','van veusen'}
b={'allen solly','mufti','wrangler','pepe jeans','lee','van heusen','monte carlo','flying machine'}
common=j.intersection(b)
print(common)



#//display the brands which are available only in begumpet branch?
j={'allen solly','wrangler','pepe jeans','levis','flying machine','allen solly','spykar','van veusen'}
b={'allen solly','mufti','wrangler','pepe jeans','lee','van heusen','monte carlo','flying machine'}
begumpet=b.difference(j)
print(begumpet)



#//display the unique brands available in the  jubille hills and begumpet branch?
j={'allen solly','wrangler','pepe jeans','levis','flying machine','allen solly','spykar','van veusen'}
b={'allen solly','mufti','wrangler','pepe jeans','lee','van heusen','monte carlo','flying machine'}
unique=j.symmetric_difference(b)
print(unique)

###########################################################################################################################################

a={'venkat','vishnu','sarma','pavana','leena'}
b={'srinu','lakshmi','venkat','sarma','ravali'}

#//now find how many empolyee are working?
working=a.union(b)
print('employee working:',len(working))
print(working)


#//display the employee names who are working in both branches?
empolyeenames=a.union(b)
print(empolyeenames)


#//display the employee names who are working only in branch-B?
b_branche=b.difference(a)
print(b_branche)


#//display all employees except common employee names?
except_common=a.symmetric_difference(b)
print(except_common)


#//display how many many employees are working  only in BRANCH-A?
branch_a=a
print('branch-A working employees is:',len(branch_a))
print(a)


#//display how many many employees are working  only in BRANCH-B?
branch_b=b
print('branch-B working employees is:',len(branch_b))
print(b)


#//display how many employee are working in both branches?
both_branches=len(a)+len(b)
print('Both branches total working employees is:',(both_branches))
