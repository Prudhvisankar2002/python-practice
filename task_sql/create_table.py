import sqlite3 as sql
con=sql.connect('amazon')
cur=con.cursor()
q="create table emp(eid int primary key,ename text,salary real,dno int )"
cur.execute(q)
con.close()

import sqlite3 as sql
con=sql.connect('amazon')
cur=con.cursor()
q="insert into emp values(101,'prudhvi',70000.0,10)"
cur.execute(q)
con.commit()
print('record inserted')
con.close()



import sqlite3 as sql
con=sql.connect('amazon')
cur=con.cursor()
q="insert into emp values(?,?,?,?)"
eid=int(input("enter id: "))
ename=input("enter emp name: ")
salary=float(input("enter emp salary: "))
dno=int(input("enter dept_no: "))
t=(eid,ename,salary,dno)
cur.execute(q,t)
con.commit()
print('record inserted')
con.close()


import sqlite3 as sql
ch='y'
while ch=='y':
    con=sql.connect('amazon')
    cur=con.cursor()
    q="insert into emp values(?,?,?,?)"
    eid=int(input("enter id: "))
    ename=input("enter emp name: ")
    salary=float(input("enter emp salary: "))
    dno=int(input("enter dept_no: "))
    t=(eid,ename,salary,dno)
    cur.execute(q,t)
    con.commit()
    print('record inserted')
    ch=input('Do you want ADD Another employee Details ? (y/n): ')
    con.close()


import sqlite3 as sql
con=sql.connect('amazon')
cur=con.cursor()
q="update emp set dno=? where eid=?"
eid=int(input("enter employee eid :"))
dno=int(input("enter employee dno :"))
t=(dno,eid)
cur.execute(q,t)
con.commit()
print('record updated')
con.close()


#//w.a.p. display the data from database
import sqlite3 as sql
con=sql.connect('amazon')
cur=con.cursor()
q="select* from emp"
cur.execute(q)
data=cur.fetchall()
print(data)
con.commit()
con.close()



import sqlite3 as sql
con=sql.connect('amazon')
cur=con.cursor()
q="select* from emp"
cur.execute(q)
data=cur.fetchall()
for i in data:
    for j in i:
       print(j,end='\t')
    print()
con.commit()
con.close()
