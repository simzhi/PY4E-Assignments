hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
frate = float(rate)
if h <= 40 :
    pay = h*frate
else :
    pay = 40*frate + (h - 40)*1.5*frate
print(pay)
