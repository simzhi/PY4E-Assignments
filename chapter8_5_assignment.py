fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    pieces = line.split()
    #print(pieces)
    if len(pieces) >=2 and 'From' in pieces:
        print(pieces[1])
        count = count + 1
    else:
        continue
print("There were", count, "lines in the file with From as the first word")
