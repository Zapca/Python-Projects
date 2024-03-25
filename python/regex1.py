import re
fname=input('Enter a filename:')
if len(fname)<1: 
    fname='sample_data.txt'
fhand=open(fname,'r')
nos=[]
for line in fhand:
    line=line.strip()
    nos.extend(re.findall('([0-9]+)',line))
integers=[float(i) for i in nos ]
print('There are',len(nos),'values and the sum=',sum(integers))
