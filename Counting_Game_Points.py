n=4
print("===Counting Game Points(n =",n,"rounds)===")
print()
#--Part 2:Formula way-always 1 step------------------------
#Algorithm:Use the shortcut formula to get the answer intasntly
#Psuedocode:total=n*(n+1)/2
#Time cost:1 step-stays the same no matter how big n is
#Space cost:1 variable(total)
total=n*(n+1)//2
print("Formula way:total",total,"| steps=1")
total=0
steps=0
for round_num in range(1,n+1):
    total+=round_num
    steps+=1
print("Loop way:total=",total,"| steps=",steps)
total=0
steps=0
for round_num in range(1,n+1):
    for points in range(1,round_num+1):
        total+=1
        steps+=1
print("Nested loop:",total,"| steps=",steps)