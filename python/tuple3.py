import string
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
with open(fname,'r') as fhand:
    doc={}
    for line in fhand:
        line=line.lower().rstrip().split()
        for word in line:
            word=word.translate(word.maketrans('','',string.punctuation))
            word=[i for i in word if not i.isdigit()]
            for str in word:
                doc[str]=doc.get(str,0)+1
lst=[(v,k)for k,v in doc.items()]
[print(y,x,)for x,y in sorted(lst,reverse=True)]