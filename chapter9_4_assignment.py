name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
emaillst = list()
for line in handle:
    line = line.rstrip()
    emails = line.split()
    if len(emails) < 3 or emails[0] != 'From':
        continue
    else:
        emaillst.append(emails[1])

for email in emaillst:
    counts[email] = counts.get(email, 0) + 1
bigcount = None
bigemail = None
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email
print(bigemail,bigcount)
