def count(x,y):
    var = 0
    x=x.split()
    for extra in x:
        if extra == y:
            var = var + 1
    return("Count",var)

word =input("Enter a string: ")
letter=input("Enter a letter: ")
print(count(word,letter))