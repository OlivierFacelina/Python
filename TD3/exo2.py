#Exo 2 

#Point 1

nb = int(input("Saisir un nombre"))
nb2 = int(input("Saisir un deuxième nombre"))

if nb > 0 and nb2 < 0 or nb < 0 and nb2 > 0:
    print('Produit négatif')
elif nb > 0 and nb2 > 0 or nb < 0 and nb2 < 0: 
        print('Produit positif')

#Point 2

if nb > 0 and nb2 < 0 or nb < 0 and nb2 > 0:
    print('Produit négatif')
elif nb > 0 and nb2 > 0 or nb < 0 and nb2 < 0: 
    print('Produit positif')
elif nb == 0 or nb2 == 0:
    print('Produit nul')