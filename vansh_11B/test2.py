t = [6,3,'h','j',"apple",6,'abc','k',9,'p']

t1= []

for i in range (3):
    t1.append(t[i])

for i in range (len(t), len(t)-3,-1):
    t1.append (t[i-1])

print(t1)
