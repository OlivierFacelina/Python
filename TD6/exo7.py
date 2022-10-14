#Exo 7 

i = list(input('Saisir 20 nombres :').split())
print(max(i))

#Correction

list = []
for i in range(1,21):
    list.append(int(input(f'Saisir un chiffre: {i}')))
maxi = max(list)
print(f"Le max est {max(list)}")