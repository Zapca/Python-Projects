try:
    hrs=float(input("Enter Hours:"))
    rate=float(input("Enter Hourly Rate:"))
except :
    print("please Enter a Valid No.!!!")
    quit ()
if hrs>40:
    x=hrs-40
    p=x*1.5*rate
    total=40*rate
    pay=total+p
    print(pay)
else:
    pay=hrs*rate
    print(pay)