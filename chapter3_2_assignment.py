hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    frate = float(rate)
except:
    print("Error, not a number!")
    quit()

if h <= 40 :
    pay = h*frate
else :
    pay = 40*frate + (h - 40)*1.5*frate
print(pay)
