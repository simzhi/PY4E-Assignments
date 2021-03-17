import re
name = input("Enter file:")
if len(name) < 1 :
    name = "regex_sum_1173873.txt"
handle = open(name)
sum = 0
for line in handle:
    number = re.findall('[0-9]+', line)
    number = [int(i) for i in number]
    for xx in number:
        sum = sum + xx
print(sum)
    #sum = sum + smallsum


#print(sum)
