import re
fname=input('Enter a filename:')
if len(fname)<1: fname='mbox-short.txt'
user_input=input('Enter a regular expression:')
with open(fname,'r') as fhand:
    exno=[]
    for line in fhand:
        line=line.strip()
        exno.extend(re.findall(user_input,line))
print(fname,'had',len(exno),'lines that matched',user_input)