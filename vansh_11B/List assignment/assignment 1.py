n = int(input("Enter the number of elements:"))
numbers = []
largest = 0
largest = 0
for i in range (n):
    numbers.append(int(input("Enter the number:")))

for num in numbers:
    if num> largest:
        largest2 = largest 
        largest = num
    elif num> largest2:
        largest2 = num


print (largest2)
