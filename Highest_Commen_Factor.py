num1=float(input("Please Enter the First Value Num1:"))
num2=float(input("Please Enter the Second Value Num2:"))
while(num2!=0):
    temp=num2
    num2=num1%num2
    num1=temp
hcf=num1
print("HCF of num1 and num2 is:", hcf)