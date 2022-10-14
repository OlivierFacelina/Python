number = int(input('Veuillez saisir un nombre'))
facture1 = 0.10 * number
facture2 = 0.19 * number
facture3 = 0.27 * number

if number <= 10:
    print('La facture est de',facture1)
elif number <= 30:
    print('La facture est de', facture2)
elif number > 30:
    print('La factur est de', facture3)

# # Correction

# number = float(input('Combien de photocopies voulez-vous ?'))
# #Cas de figure où l'utilisateur choisit 10 ou moins de photocopies
# if number <= 10:
#     price = 0.10 * number
# elif number <= 30:
#     price = (0.09 * (number-10) + (10*0.10))
# else:
#     price = (0.08 * (number-30) + (20*0.09) + (10*0.10))
# print(f'Le prix total de votre commande est de {price} euros ')