name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
emaillst = list()
hourlist = list()

for line in handle:
    line = line.rstrip()
    emails = line.split()
    if len(emails) < 3 or emails[0] != 'From':
        continue
    else:
        emaillst.append(emails[5])
for time in emaillst:
    time = time.split(':')
    hourlist.append(time[0])
for hour in hourlist:
    counts[hour] = counts.get(hour, 0) + 1
counts = sorted(counts.items())
for k,v in counts:
    print(k,v)
