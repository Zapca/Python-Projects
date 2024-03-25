fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('From '):
        line=line.split()
        print(line[1])
        count+=1
    continue
print("There were", count, "lines in the file with From as the first word")