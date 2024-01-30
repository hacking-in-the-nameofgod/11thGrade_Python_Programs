n = int(input("Enter the number of elements to be added: "))

a = []
b = []

for i in range (n):
    a.append(int(input("Enter the number:")))

for x in a [::-1]:
    b.append(x)

print (b)
