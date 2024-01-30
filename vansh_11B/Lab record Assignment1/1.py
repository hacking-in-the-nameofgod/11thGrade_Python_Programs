print ()
print ("Income Tax Calculator")

print ()

income = int(input("Enter your moneys in INR:"))

print ()

if income>0 and income<=300000:
    tax_rate=0.0

elif income>300000 and income<= 600000:
    tax_rate=0.05

elif income>600000 and income <= 900000:
    tax_rate=0.10

elif income>900000 and income <= 1200000:
    tax_rate=0.15

elif income>1200000 and income<= 1500000:
    tax_rate=0.20

elif income>1500000:
    tax_rate = 0.30

else:
    print("Error")


base_tax= tax_rate*income

print ("Basic Income Tax" , base_tax)

total_basetax = income + base_tax

print()

if income>5000000 and income<10000000:
    surcharge = 0.10 * base_tax

elif income >= 10000000:
    surcharge = 0.15*base_tax

else:
    surcharge = 0

print ("Surcharge is:", surcharge)

print()

cess = 0.03*base_tax

print ("Cess is:" , cess)

print()

total= base_tax + surcharge + cess

print ("Total tax owed:" , total)

print()

tds = total/12

print ("TDS:" , tds)

print()



print ("Pay taxes on time.")
print()



