fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find(':')
    value = value + float(line[pos+1:])
    # print(line)
print("Average spam confidence:", value/count)
