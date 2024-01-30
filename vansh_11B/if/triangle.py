side1 = float(input("Length of 1st side:"))
side2 = float(input("Length of 2nd side:"))
side3 = float(input("Length of 3rd side:"))

a = side1 + side2
b = side2 + side3
c = side3 + side1

if a>side3 and b>side1 and c>side2:
    print ("Triangle is possible.")

else:
    print ("Triangle is not possible.")


