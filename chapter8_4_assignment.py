fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    pieces = line.split()
    for word in pieces:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
