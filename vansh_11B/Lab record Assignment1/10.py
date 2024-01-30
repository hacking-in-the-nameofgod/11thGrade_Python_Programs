llimit = int(input("Enter Integer Lower Limit:"))
ulimit = int(input("Enter Integer Upper Limit:"))
print ()

for x in range (llimit,ulimit+1,1):
    a = x
    sum1 =0
    sum2=0
    for y in range (1, x, 1):
        if x%y ==0:
            sum1 += y
        

    cpofsum1= sum1

    for z in range (1,sum1):
        if sum1%z ==0:
            sum2 += z

      

    if sum2 == x:
        print (x,cpofsum1)

   
