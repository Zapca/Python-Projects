def computepay(h, r):
    if h>40:
        pay=h*r
        overtime=(h-40)*(0.5*r)
        return(pay+overtime)
    else:
        pay=h*r
        return pay
try:
    hrs=float(input("Enter Hours:"))
    rate=float(input("Enter Rate:"))
except:
    print("Please Enter a Valid Number!")
    quit()
p=(computepay(hrs,rate))
print("Pay", p)