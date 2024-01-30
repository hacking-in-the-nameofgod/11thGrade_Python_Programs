import random

n = int(input("Enter the number of elements in the given list: "))
z = 0
org = []

for i in range (n):
    org.append(int(input("Enter the element: ")))

use = org

while z != 4:
    use = org
    print ('''Options:
1. Sorting
2. Display
3. Shuffle
4. Exit''')

    opt = int(input("Enter option no. : "))

#bubble sort:
    
    if opt == 1:
        print ('''Options:
1. Bubble Sort
2. Insertion Sort''')
        opt2 = int(input("Enter the option no. : "))

        if opt2 == 1:
            print ('''Options:
1. Ascending
2. Descending''')

            opt3 = int(input("Enter the option no. : "))
#ascending
            if opt3 == 1:

                for i in range (n):
                    for j in range (n-1):
                        if use[j] > use[j+1]:
                            use[j] , use[j+1] = use[j+1] , use[j]

                print (use)
#descending
            elif opt3 == 2:
                for i in range (n):
                    for j in range (n-1):
                        if use[j] < use[j+1]:
                            use[j] , use[j+1] = use[j+1] , use[j]
                print (use)
            else:
                print("Error")
#insertion

        elif opt2 ==2:
            print ('''Options:
1. Ascending
2. Descending''')

            opt4 = int(input("Enter the option number:"))
#ascending
            if opt4 ==1:
                for q in range(n):
                    for w in range(0,q):
                        if use[q]<use[w]:
                            use[q], use[w] = use[w], use[q]
                print(use)
#descending
            elif opt4 == 2:
                for q in range(n):
                    for w in range (0,q):
                        if use[q]>use[w]:
                            use[q], use[w] = use[w] , use[q]
                print(use)

            else:
                print("Error")
        else:
            print("Error")
            
#display
    elif opt == 2:
        print (org)

#shuffle
    elif opt == 3:
        for e in range(0, n-1):
            y = random.randint(0,n-1)
            use[e], use[y] = use[y] , use[e]
        print(use)
#exit
    elif opt == 4:
        print("Exiting")
        break

    else:
        print("Error")


        
                        

            
