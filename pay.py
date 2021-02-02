hrs=input('enter hours:')
h=float(hrs)
rate=input('enter rate:')
r=float(rate)
if h<=40:
    pay=h*r
else:
    pay1=h*r
    extra=(h-40)*(r*0.5)
    pay=pay1+extra
print(pay)
