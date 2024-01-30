N = int(input("Ënter N:"))
z = int(input("Ënter z:"))
sin = 0

for x in range (1, 2*N+1,2):
    sui = 1
    a=x
    while x>0:
        sui *= x
        x = x-1
    x = a
    sin += ((-1)**(x+1))*(z**x/sui)

print (sin)
