print ("Find the roots of a quadratic equation")

print ("")


a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

print ("")

d = (b**2 - 4*a*c)**0.5

soln1 = (d-b) / 2*a

soln2 = -(d+b) / 2*a

print ("The solutions of the given equation are:", soln1 , soln2)
