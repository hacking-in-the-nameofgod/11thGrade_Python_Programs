N = int(input("Ënter N:"))
z = int(input("Ënter z:"))
cos = 0
z= (z*180 /3.14)

for x in range (0, 2*N ,2):
    sui = 1
    a=x
    while x>0:
        sui *= x
        x = x-1
    x = a
    cos += (((-1)**(a))*((z**x)/sui))
    print (cos)
print (cos)
    





    
