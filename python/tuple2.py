fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhand = open(fname)
doc={}
for line in fhand:
    if line.startswith("From "):
        line=line.rstrip().split()
        word=line[5].split(':')
        doc[word[0]]=doc.get(word[0],0)+1
x=sorted(doc.items())
for i,j in x:
    print(i,j)