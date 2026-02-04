print("Enter Marks Obtained in 5 subjects:")
markOne=int(input())
markTwo=int(input())
markThree=int(input())
markFour=int(input())
markFive=int(input())
tot=markOne+markTwo+markThree+markFour+markFive
avg=tot/5
if avg>=91 and avg<=100:
    print("Your grade is A1")
elif avg>=81 and avg<91:
    print("Your grade is A2")
elif avg>=71 and avg<81:
    print("Your grade is B1")
elif avg>=61 and avg<71:
    print("Your grade is B2")

