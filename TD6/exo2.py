#Exo 2 

i = int(input('Saisir un nombre'))

while i >= 10 and i <= 20:
    print(i)
    i = i + 1

if i < 10:
    print('Plus grand !')
elif i > 20: 
    print('Plus petit !')

#Correction

# numbers = 0
# while numbers > 20 or numbers < 10 :
#     numbers = int(input('Choisissez un nombre :'))
#     if numbers > 20 :
#         print('Plus petit !')
#     if numbers < 10 :
#         print('Plus grand')
