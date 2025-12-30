import pyodbc as sql
con=sql.connect(driver='SQL Server',server='PRUDHVISANKAR',database='amazon1',user='sa',password=2002)
print(con)
con.close()



import pyodbc as sql
con=sql.connect(driver='SQL Server',server='PRUDHVISANKAR',database='redbus',user='sa',password=2002)
print(con)
con.close()


s1=int(input('enter subject-1 marks: '))
s2=int(input('enter subject-2 marks: '))
s3=int(input('enter subject-3 marks: '))
total=s1+s2+s3
average=((s1+s2+s3)/3)
for i in average:
    if i>=80 and i<=100:
        grade='A'
    elif i>=60 and i<=79:
        grade='B'
    elif i>=40 and i<=59:
        grade='C'
    elif i>=35 and i<=39:
        grade='D'
    else:
        grade='Fail'
print(grade)



