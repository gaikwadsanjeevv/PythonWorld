high_income = True
good_credit = False
student = True

if high_income  and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

if not student:
    print("Eligible")
else:
    print("Not eligible")

if(high_income or good_credit) and not student:        #when the evaluation stops when one  of the argument is false is short-circuit evaluation, in python the logical operators are SCE
    print("Eligible")
else:
    print("Not Eligible")