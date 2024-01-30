n = int(input("Enter number of times to add:"))
ts = 0 
for x in range (1,n+1,1):
    s = 0
    while x>0:
        s+=x
        x-=1

    ts += s

    
print (ts)
