
print ("Teliance Company bill")

print ()

units= int(input("Enter no. of units consumed: "))



if units>= 0 and units <= 100:
    amt= 2.96*units

elif units>=101 and units <=300:
    amt = 296 + (5.56*(units-100))

elif units>= 301 and units <= 500:
    amt = (296 + 1112 + (9.16*(units-300)))

elif units>= 501:
    amt = (296+1112+1832 + (10.61*(units-500)))

else:
    print ("ERROR")


print ("Base amount:", amt)

if amt>=1000:
    surcharge = 0.15*amt

else:
    surcharge = 0

print ("Surcharge:", surcharge)


total_amt = surcharge + amt

if total_amt> 100:
    total_amt = total_amt

else:
    total_amt = 100





print ("Total Bill amout:" , total_amt , "inr")

print ("Pay bills on time.")





