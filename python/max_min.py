lst=list()
while True:
    value=input('Enter a number:')
    if value=='done': break
    try : value=float(value)
    except: print('Fuck you jason , type a number or done not any Bullshit')
    lst.append(value)
print("Maximum:",max(lst))
print("Minimum:",min(lst))