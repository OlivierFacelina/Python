#Exo 4  

# while True:
#     number1 = int(input('Saisir un autre entier'))
#     number2 = int(input('Saisir un autre entier'))
#     somme = number1 + number2
#     print(somme)
#     if number1 == 0 or number2 == 0: 
#         print('Tu as saisi un zéro')
#         break

#Correction

i, total = int(input('Saisir un nombre :')), 0
while i != 0:
    total += total # total = total + 1
    i = int(input('Saisir un autre nombre :'))
print(i)