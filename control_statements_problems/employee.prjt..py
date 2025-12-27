annualsalary=float(input('Enter the annual salary: '))
monthlysalary=annualsalary/12
if monthlysalary>=25000:
   experience=int(input('Enter the experience: '))
   if experience>=2:
      print('1.education loan')
      print('2.gold loan')
      print('3.house loan')
      choice=int(input('Enter your choice: '))
      if choice==1:
          print('education loan')
          print('intrest amount is= 4.8')
          intrest=4.8
      elif choice==2:
          print('gold loan')
          print('intrest amount is= 8.9')
          intrest=8.9
      elif choice==3:
          print('house loan')
          print('intrest amount is= 18.5')
          intrest=18.5
      else:
          print('invalid choice')
      amount=float(input('Enter your  loan amount: '))
      duration=int(input('Enter the duration: '))
      simple_intrest=amount*duration*intrest/100
      print('intrest amount is:',simple_intrest)
      total=simple_intrest+amount
      print('final total amount is:',total)
      emi=total/(duration*12)
      print(' monthly emi amount is:',emi)


   else:
       print('sorry..your loan application rejected.. Due to less experience')
else:
    print('sorry.. loan rejected..Due to less salary')