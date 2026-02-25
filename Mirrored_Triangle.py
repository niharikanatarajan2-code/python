rows=int(input("Enter rows:"))
for i in range(rows):
    spaces=rows-i-1
    stars=i+1
    print(" "*spaces+"*"*stars)