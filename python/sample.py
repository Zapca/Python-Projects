import string
fname=input('Enter a name:')
fhand=open(fname,'r')

doc={}

for line in fhand:
    #line=line.translate(line.maketrans('','',string.punctuation))
    # remember that i spent whole day for making a mistake of "From" and not "Form " spaces are important
    if line.startswith("From "):
        line=line.rstrip().split()
        word=line[1].split('@')[1]
        doc[word]=doc.get(word,0)+1

q=None
w=None
for i,j in doc.items():
    if w is None or w<j:
        q=i
        w=j
print(q,w)