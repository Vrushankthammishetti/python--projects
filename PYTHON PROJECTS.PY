units=int(input("enter electricity units:"))
if units <=100:
    bill=units*1.5
elif units<=200:
    bill=units*2.5
elif units <=300:
    bill=units*4.5
else:
    bill=units*5

print("Electricitry Bill=",bill)