fname = input("Enter a name:")
with open(fname, "r") as fhand:
    doc = {}
    for line in fhand:
        if line.startswith("From "):
            line = line.strip().split()
            doc[line[1]] = doc.get(line[1], 0) + 1
    print(max(doc,x=doc.get))