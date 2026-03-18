try:
    age=int(input("Enter your age: "))
    if age<=0 or age>120:
        print("Invalid age entered.")
    else:
        print("Valid age")
        if age%2==0:
            print("The age is even.")
        else:
            print("The age is odd.")
except ValueError:
    print("Invalid input!Please enter a number.")