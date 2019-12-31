def computepay(h,r):
    gp=0
    if (h<=40):
        gp=h*r
    else:
        gp=40*r+(h-40)*r*1.5
    return gp

hrs = input("Enter Hours:")
pr = input("Enter Pay:")
h=float(hrs)
p=float(pr)
gp = computepay(h,p)
print(gp)
