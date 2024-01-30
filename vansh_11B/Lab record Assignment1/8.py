for x in range (1,1001):
    for y in range (x+1):
        for z in range (y+1):
            if y!= 0 and z!=0 and x!=0 and y**2 + z**2 == x**2:
                print (z,y,x)
