a = int(input("Days for which book was borrowed:"))


if a>0 and a<= 5:
    cost = a*2

elif a > 5 and a<= 10:
    cost = (((a-5)*3) + (5*2))

elif a>10 and a<=15:
    cost = ((5*2) + (5*3) + ((a-10)*4))

elif a>15:
    cost = ((5*2) + (5*3) + (5*4) + ((a-15)*5))

else:
    print ("Invalid Input.")
    cost = "Invalid"


print ("The cost is:" , cost)

