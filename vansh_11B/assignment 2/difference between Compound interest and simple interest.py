p = int(input("Enter principal amount borrowed:"))

r = int(input("Enter Rate of intrest at which loan is taken:"))

n = int(input("Enter time for which loans is take (in years)"))

si=p*n*r/100

ci= (p*((1 + (r/100))**n)) - p

print("")
print ("")
print ("Simple Intrest:", si)
print ("Compund Intrest:", ci)


print ("")

print ("Difference between Compund intrest and Simple Intrest is:" , ci-si)

