n = int(input("Enter the number of elements in list: "))
b = []
opt = 0
for i in range (n):
    b.append(input("Enter the Element: "))

while opt != 4:
    print('''
1. Reverse each element of the list and display it. 
2. Swap the consequent elements of the list and display it.
3. Display List
4. exit''')
    opt = int (input("Enter the option number: "))

    if opt == 1 :
        for q in range (len(b)):
            b[q] = b[q][::-1]

        print(b)

    elif opt == 2 :
        print(b)
        for w in range (0,len(b),2):
            if w+1 >= len(b):
                break
            b[w], b[w+1] = b[w+1], b[w]
        print (b)

    elif opt == 3:
        print (b)

    elif opt == 4:
        break 