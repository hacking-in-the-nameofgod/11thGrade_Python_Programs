n = int(input("Number of records to be stored: "))
b = []
opt = 0
for i in range (n):
    temp = []
    for w in range(3):
        temp.append(input("Enter elements:"))
    q = tuple(temp)
    b.append(q)

q = tuple(b)

print(q)

while opt != 4:
    print('''
1) In Alphabetical order of the employee names 
2) In ascending order of the Age 
3) In descending order of the Salary''')

    opt = int(input("Enter option: "))

    if opt == 1:
        for y in range (n):
            for i in range(n):
                if i+1 >= n:
                    break
                if b[i][0] > b[i+1][0]:
                    b[i], b[i+1] = b[i+1], b[i]

        print (tuple(b))
    
    elif opt == 2:
        for y in range (n):
            for i in range(n):
                if i+1 >= n:
                    break
                if int(b[i][1]) > int(b[i+1][1]):
                    b[i], b[i+1] = b[i+1], b[i]

        print (tuple(b))

    
    elif opt == 3:
        for y in range (n):
            for i in range(n):
                if i+1 >= n:
                    break
                if int(b[i][2]) < int(b[i+1][2]):
                    b[i], b[i+1] = b[i+1], b[i]

        print (tuple(b))