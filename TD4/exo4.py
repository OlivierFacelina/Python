# candidat = int(input('Veuillez saisir le numéro du candidat'))
# score = float(input('Veuillez saisir le score'))

# if candidat != 1:
#     print('Mauvais candidat, désolé')
# if score > 50:
#     print('Ce candidat est élu dès le premier tour')
# elif score >= 12.5 and score <= 50:
#     print('Ce candidat se trouve en ballotage favorable')
# else:
#     print('Ce candidat est battu')

#Correction

candidat1 = float(input('Pourcentage du 1e candidat'))
candidat2 = float(input('Pourcentage du 2e candidat'))
candidat3 = float(input('Pourcentage du 3e candidat'))
candidat4 = float(input('Pourcentage du 4e candidat'))
somme = candidat1 + candidat2 + candidat3 + candidat4

if somme <= 100:
    if candidat1 >= 50:
        print('Le premier candidat est élu')
    elif candidat2 >= 50 or candidat3 >= 50 or candidat4 >= 50:
        print('Le premier candidat est battu')
    elif candidat1 >= 12.5 and candidat1 > candidat2 and candidat1 > candidat3 and candidat1 > candidat4:
            print('Le premier candidat se trouve en ballotage favorable')
    else:
            print('Le premier candidat se trouve en ballotage défavorable')
else: 
    print('Il y a eu triche')