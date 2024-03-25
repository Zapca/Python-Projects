value=input('Enter a character: ')
uc=len(value)
count=None
while True:
    if count is None:
        count=uc-1
        print(value[count])
        continue
    elif count>0:
        count=count-1
        print(value[count])