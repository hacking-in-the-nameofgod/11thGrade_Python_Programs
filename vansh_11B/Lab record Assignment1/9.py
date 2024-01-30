n = int(input("Enter no. of lines of pattern:"))

#p1
for x in range (1,n+1):
    y=1
    print()
    while y<=x:
        print (y, end=" ")
        y+=1


print ()
print ()

# p2

for x in range (n,0,-1):
    y=1
    print()
    while y<=x:
        print (y, end=" ")
        y+=1

print ()
print ()

#p3
for x in range (1,n+1):
    y=1
    print()
    for z in range (n-x+1,1,-1):
        print (" ", end =" ")
    while y<=x:
        print (y, end=" ")
        y+=1

print ()
print ()

#P4
for x in range (n,0,-1):
    y=1
    print()
    for z in range (n-x):
        print (" ", end = " ")
    while y<=x:
        print (y, end=" ")
        y+=1

print ()
print ()
#p5


