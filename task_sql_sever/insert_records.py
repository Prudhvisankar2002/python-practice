 import pyodbc as sql
con=sql.connect(driver='SQL Server',server='PRUDHVISANKAR',database='redbus',user='sa',password=2002)
print(con)
cur=con.cursor()
q="insert into student values(?,?,?,?,?,?,?,?)"
sid=int(input('enter student id: '))
sname=input('enter student name: ')
gender=input('enter gender (M/F/O)?: ')
s1=int(input('enter subject-1 marks: '))
s2=int(input('enter subject-2 marks: '))
s3=int(input('enter subject-3 marks: '))
total=s1+s2+s3
average=float((s1+s2+s3)/3)
t1 = (sid, sname, gender, s1, s2, s3, total, average)
cur.execute("alter table student add grade varchar(2);")
cur.execute("select average from student")
data=cur.fetchall()
for i in data:
    if i.average>=90:
        grade='A'
    elif i.average>=80:
        grade='B'
    elif i.average>=70:
        grade='C'
    elif i.average>=50:
        grade='D'
    else:
        grade='Fail'
    q1="update student set grade='?' where sid=?"
    t2=()
    cur.execute(q,t1,)
con.commit()
print('record inserted')
con.close()





import pyodbc as sql
con=sql.connect(driver='SQL Server',server='PRUDHVISANKAR',database='redbus',user='sa',password=2002)
print(con)
cur = con.cursor()
sid = int(input("Enter Student ID: "))
sname = input("Enter Student Name: ")
gender = input("Enter Gender(m/f/o): ")
s1 = int(input("Enter Subject 1 Marks: "))
s2 = int(input("Enter Subject 2 Marks: "))
s3 = int(input("Enter Subject 3 Marks: "))
total = s1 + s2 + s3
average = total / 3
try:
    cur.execute("alter table student add grade varchar(2)")
    con.commit()
except:
    pass
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 50:
    grade = 'D'
else:
    grade = 'F'
q="insert into student values(?, ?, ?, ?, ?, ?, ?, ?, ?)"
t1=(sid, sname, gender, s1, s2, s3, total, average, grade)
cur.execute(q,t1)
con.commit()
print(" record inserted with Grade")
con.close()
