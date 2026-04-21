class Animal:
    species="dog"
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
Bob=Animal("Bob","Labradour",5)
Mity=Animal("Mity","German Shepard",3)
print("Bob is a {}".format(Bob.species))
print("Mity is also a {}".format(Mity.species))
print("{} is {} years old".format(Bob.name,Bob.age))
print("{} is {} years old".format(Mity.name,Mity.age))
