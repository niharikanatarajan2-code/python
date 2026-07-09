names=["Aarav","Priya","Dev","Meera","Kabir"]
scores=[90, 75, 88, 62, 95]
n=len(scores)
print("===Score Tracker(n=",n,"players)===")
for i in range(n):
    print(i+1,".",names[i],":",scores[i],sep="")
    print()
steps=1
print("Score at index 0:",scores[0],"| steps=",steps,"| Theta(1)-tight bound")
print()
target="Aarav"
steps=0
for name in names:
    steps+=1
    if name==target:
        break
print("Search for",target,"| steps=",steps,"| Omega(1)-best case lower bound")
target="Kabir"
steps=0
for name in names:
    steps+=1
    if name==target:
        break
print("Search for",target,"| steps=",steps,"| O(n)=",n,"-worst upper case bound")
print()