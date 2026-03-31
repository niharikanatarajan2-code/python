start=(input("Enter start:"))
end=(input("Enter end:"))
squares=[]
even=[]
odd=[]
for num in range(start,end):
    sq=num*num
    squares.append(sq)
    if sq %2==0:
        even.append(sq)
    else:
        odd.append(sq)
print("Squares:",squares)
print("Even Squares:",even)
print("Odd Squares:",odd)