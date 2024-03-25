largest=None
Smallest=None
while True:
    num=input('Enter a number: ')
    if num == "done":
        break
    try:
        value=float(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest=value
    elif largest<value:
        largest=value
    if Smallest is None:
        Smallest=value
    elif Smallest>value:
        Smallest=value
print("Maximum is", largest)
print("Minimum is", Smallest)