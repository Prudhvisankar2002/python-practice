# import pyodbc as sql
# con=sql.connect(driver='SQL Server',server='PRUDHVISANKAR',database='amazon1',user='sa',password=2002)
# print(con)
# cur=con.cursor()
# q="insert into emp values(111,'prudhvi','m',70000.0)"
# cur.execute(q)
# con.commit()
# print('record inserted')
# con.close()


##//read a  mutilple values from user to insert the values into table from sql server?
# import pyodbc as sql
# ch='y'
# while ch=='y':
#     con=sql.connect(driver='SQL Server',server='PRUDHVISANKAR',database='amazon1',user='sa',password=2002)
#     print(con)
#     cur=con.cursor()
#     q="insert into emp values(?,?,?,?)"
#     eid=int(input("enter employee id: "))
#     ename=input("enter employee name: ")
#     gender=input("enter employee gender(M/F/O): ")
#     salary=float(input("enter employee salary: "))
#     t1=(eid,ename,gender,salary)
#     cur.execute(q,t1)
#     con.commit()
#     print('record inserted')
#     ch=input('Do you want ADD another employee record?(y/n): ')
#     con.close()


##//read the data from user to update records into table of the sql sever?
# import pyodbc as sql
# con=sql.connect(driver='SQL Server',server='PRUDHVISANKAR',database='amazon1',user='sa',password=2002)
# print(con)
# cur=con.cursor()
# q="update emp set salary=? where eid=?"
# eid=int(input('enter employee id: '))
# salary=float(input('enter employee salary: '))
# t1=(salary,eid)
# cur.execute(q,t1)
# con.commit()
# print('record updated')
# con.close()


##//read emp id  delete the record from user to record from sql sever?
# import pyodbc as sql
# con=sql.connect(driver='SQL Server',server='PRUDHVISANKAR',database='amazon1',user='sa',password=2002)
# print(con)
# cur=con.cursor()
# q="delete from emp where eid=?"
# eid=int(input('enter employee id: '))
# t1=(eid,)
# cur.execute(q,t1)
# con.commit()
# print('record deleted')

# con.close()




# import pyodbc as sql
# con=sql.connect(driver='SQL Server',server='PRUDHVISANKAR',database='amazon2',user='sa',password=2002)
# print(con)
# cur=con.cursor()
# subject=input('enter which subject to change(s1/s2/s3): ')
# m=int(input('enter the  new marks: '))
# sid=int(input('enter the student id: '))
# if subject in ('s1','s2','s3'):
#     q=f"UPDATE student2 SET {subject} = ? WHERE sid = ?"
#     t1=(m,sid)
#     cur.execute(q,t1)
#     con.commit()
#     print('record inserted')
#     con.close()




# import pyodbc as sql
# con=sql.connect(driver='SQL SERVER',server='PRUDHVISANKAR',database='amazon2',user='sa',password='2002')
# print(con)
# cur=con.cursor()
# from_acno=int(input("Enter FROM account number: "))
# to_acno=int(input("Enter TO account number: "))
# amount=float(input("Enter amount: "))
# cur.execute("select amount from customer where acno=?",(from_acno,))
# data=cur.fetchone()
# if data is None:
#     print('from is account is not found')
# else:
#     balance=data[0]
#     if amount<=balance:
#         cur.execute("update customer set amount=amount-? where acno=?",(amount,from_acno))
#         cur.execute("update customer set amount=amount+? where acno=?",(amount,to_acno))
#         con.commit()
#         print('transaction completed successfully')
#     else:
#         print(amount,'is less not provide to do transaction')
#         con.close()

























