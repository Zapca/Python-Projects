import re
fname=input('Enter a filename:')
if len(fname)<1: 
    fname='sample_data.txt'
# fhand=open(fname)
print(sum([for line in fhand (re.findall('[0-9]+',line))with open(fname,'r')as fhand]))
