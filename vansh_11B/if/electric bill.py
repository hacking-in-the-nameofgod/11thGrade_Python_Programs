units = int(input("Enter number of units consumed:"))

if units>=0 and units<=100:
    cost = 0

elif units>100 and units<=300:
    cost = (units-100)*2

elif units > 300:
    unit1 = units -300
    unit2 = (units - unit1) - 100
    cost = (unit1*5) + (unit2*2)

else:
    print ("Invalid Input")






print ("The electric bill is:" , cost)
