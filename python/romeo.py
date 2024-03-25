fname = input("Enter file name: ",'r')
fhand = open(fname)
lst = list()
for line in fhand:
    line=line.strip()
    line=line.split()
    for words in line:
        if words in lst: continue
        lst.append(words)
lst.sort()
print(lst)