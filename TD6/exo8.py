#Exo 8

i = list(input('Saisir 20 nombres :').split())
print(f'Le plus grand nombre est {max(i)} en position {i.index(max(i))}')

#Correction 

list = []
for i in range(1,21):
    list.append(int(input(f'Saisir un chiffre: {i}')))
maxi = max(list)
pos = list.index(maxi)+1
print(f"Le max est {max(list)} et sa position est {pos}")