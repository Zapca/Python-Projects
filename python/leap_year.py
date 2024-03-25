ui=int(input('Enter a Year:'))
if ui%4==0 and (ui%400==0 or ui%100!=0):
    print('leap year babyyyyy')
else:
    print('Nope')
