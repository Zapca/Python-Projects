try:
    score=float(input("Enter Score: "))
    if score>1.0:
        print("The Entered Score is Too High,Please try again!")
    elif score>=0.9:
        print("A")
    elif score>=0.8:
        print("B")
    elif score>=0.7:
        print("C")
    elif score>=0.6:
        print("D")
    elif score<6:
        print("F")
except:
    print("Entered Value is Incorrect try again!")
quit ()