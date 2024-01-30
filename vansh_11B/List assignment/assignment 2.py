n = int(input("Enter the number of elements to be enetered:"))

a = []
q = []
w = []
for i in range (n):
    a.append(int(input("Enter the number:")))

print (a)

for x in a:
    if x>=0:
        q.append(x)
    else:
        w.append(x)

print (q)
print (w)
