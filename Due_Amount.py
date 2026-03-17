bill_amount=float(input("Enter total bill amount: "))
amount_paid=float(input("Enter amount paid: "))
due_amount=bill_amount-amount_paid
if due_amount>0:
    print("Amount still due:", due_amount)
elif due_amount==0:
    print("Bill fully paid. No amount due.")
else:
    print("Extra paid. Change to return:", abs(due_amount))