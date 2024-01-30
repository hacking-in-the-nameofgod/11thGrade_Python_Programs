r = int(input("Enter the number of rows in matrix: " ))
c = int(input("Enter the number of coloumns in matrix: "))
b = []
row_count= 1
opt1 = 0



for i in range (r):

    

    a = []
    print ("Enter elements for", row_count, "row")
    for j in range (c):
        a.append(int(input("Enter the element: ")))

    b.append(a)
    row_count +=1
    
print ("matrix: ")
print()
for q in b:
    print (q)


#functionality:

while opt1 != 7:
    print()
    print()
    print (''' Select the function:
1) Swap the first and the last row elements
2) Swap the first and the last column elements
3) Find the sum of middle row elements and middle column elements (if any)
4) Sum the alternate elements of the list.(Move Row wise)
5) Transpose of the matrix
6) Display of the matrix
7) Exit''')

    exp_c = c
    exp_r = r
    sum = 0
    sum2 = 0
    
    opt1 = int(input("Enter the option: "))

#Swap the first and the last row elements

    if opt1 == 1:
        b[0],b[r-1] = b[r-1],b[0]
        for q in b:
            print (q)

#Swap the first and the last column elements

    elif opt1 == 2:
        for z in range(r):
            b[z][0], b[z][c-1] = b[z][c-1], b[z][0]
        for q in b:
            print (q)

#sum middle

    elif opt1 ==3:
        if r%2 == 1:
            for num in b[(r-1)//2]:
                sum += num
        if c%2 == 1:
            for mun in b:
                sum += mun[(c-1)//2]


        print(sum)

#sum alternate

    elif opt1 == 4:
        for a in b:
            for qw in range(0,len(a),2):
                sum2 += a[qw]

        print(sum2)


#transpose

    elif opt1 ==5:
        if c>r:
            rest = []
            for t in range (c):
                rest.append("")
                
            while exp_c>exp_r:
                b.append(rest)
                exp_r+=1
  
        elif r>c:
            while exp_r>exp_c:
                for lol in range (r):
                    b[lol].append("")
                exp_c +=1

        for w in range(exp_r):
            for e in range(w):
                b[w][e], b[e][w]= b[e][w], b[w][e]

        for el in b:
            for x in el:
                if x == "":
                    el.remove("")
                    

            if el == ['']:
                b.remove ([''])
                b.remove (['',''])

        c,r = r,c

        for q in b:
            print (q)

# print

    elif opt1 == 6:
        for q in b:
            print (q)

# End

    elif opt1 == 7:
        break

    else:
        print("Error")
