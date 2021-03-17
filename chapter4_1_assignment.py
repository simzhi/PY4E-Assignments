def computepay(h,r):
    if h <= 40:
        pay = h*r
    elif h > 40:
        pay = 40 * r + (h - 40) * 1.5 * r
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
fhrs = float(hrs)
frate = float(rate)
p = computepay(fhrs,frate)
print("Pay",p)
