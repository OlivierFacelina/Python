#Exo 5 

# i = int(input('Saisissez un entier : '))
# i2 = int(input('Saisissez un autre entier :'))
# while i in list(range(i,i2,1)):
#     i = int(input('Saisissez un entier :'))
#     i2 = int(input('Saisissez un autre entier :'))
#     somme = i + i2
#     print(somme)
#     if i == 0 or i2 == 0:
#         print('Tu as saisi un zéro')
#         break
    
#Correction

list = []
n = int(input('Saisir un autre nombre :')) 
while n != 0:
    list.append(n) # ajouter la valeur dans la liste
    n = int(input('Saisir un autre nombre :'))
print(sum(list))