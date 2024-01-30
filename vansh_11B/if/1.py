a= float(input("Enter number 1:"))
b= float(input("Enter number 2:"))
c= float(input("Enter number 3:"))

if a>=b and b>=c:
    print (b)

elif a>=c and c>=b:
    print (c)

elif b>=a and a>=c:
    print (a)

elif c>=b and b>=a:
    print (b)

elif b>=c and c>=a:
    print (c)

elif c>=a and a>=b:
    print (a)

else:
    print ("cannot comprehend")

    
