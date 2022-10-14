#Exo 2 
 
ht = float(input("Le prix d'un article hors taxe est:"))
quantity = int(input("La quantité d'article est :"))
tva = float(input("La TVA est de :"))
ttc = (ht * (1+tva/100)) * quantity
print(f"Le prix TTC est de {ttc} euros")

#Fonction pour arrondir
# num = 19.9999999999
# print("truncated = %.2f" % (int(num*100)/100))