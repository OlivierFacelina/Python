#Exo 9

# x = int(input('Saisir un premier article :'))
# if(x%2 == 0 or x%3 == 0 or x%5 ==0 or x%7 == 0 or x%9 == 0 or x%11 == 0):
#     print(x)
# else: 
#     print('Nombre qui n est pas un entier')
    
# for i in range(x, x+1):
    
#Correction 

money = [10,5,1]
back = []
price = int(input("Quel est le prix de l'article"))
total = 0
while price != 0:
    total += price
    price = int(input("Quel est le prix de votre article"))
print(f"La Somme de votre panier est : {total} euro(s)")
price3 = int(input("Combien d'argent donnez-vous :"))
dif = price3 - total
if dif // money[0]:
    back.append(money[0])
    dif -= money[0]
elif dif // money[1]:
    back.append(money[1])
    dif -= money[1]
elif dif // money[2]:
    back.append(money[2])
    dif -= money[2]
print(back)