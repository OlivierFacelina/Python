#Exo 2 

x = input('Entrez un mot :')
y = []
for i in range(len(x)):
    if ord(x[i]) > 127:
        z = (hex(ord(x[i])))
        y.append(z[2:])
print(y)