n = int(input("Enter number of terms in a list: "))
a = []

for i in range(n):
    a.append(int(input("Enter the element:")))

print (a)

for j in range (n):
    for q in range (n-1):
        if a[q+1] >= a[q]:
            a[q], a[q+1] = a[q+1] , a[q]



print (a)


