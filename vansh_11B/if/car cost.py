km = int(input("Enter distance travlled:"))

if km>0 and km<=10:
    cost = km*11

elif km>10 and km<=100:
    cost = ((km-10)*10) + (11*10)

elif km> 100:
    cost = ((11*10) + (90*10) + ((km-100)*9))

else:
    cost = "Invalid"

print ("Cost of driving is:" , cost)
