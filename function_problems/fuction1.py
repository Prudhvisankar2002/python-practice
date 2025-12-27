def calmonthsalary(annualsalary):
    monthlysalary = annualsalary/12
    return monthlysalary
monthsalary=float(input("Enter the annual salary: "))
print("monthsalary is:",calmonthsalary(monthsalary))