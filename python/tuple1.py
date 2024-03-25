fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhand = open(fname)

doc={}

for line in fhand:
    if line.startswith("From "):
        line=line.rstrip().split()
        doc[line[1]]=doc.get(line[1],0)+1

#[print(v,k)for k,v in sorted(doc.items(),reverse=True)]
lst=[]
for k,v in doc.items():
    lst.append((v,k))
    lst=sorted(lst,reverse=True)

for j,i in lst[:1]:
    print(i,j)