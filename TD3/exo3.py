#Exo 3 

age = int(input('Saisir un nombre'))

if age < 10:
    print('Microbe')
elif age < 12:
    print('Poussin')
elif age < 14:
    print('Benjamine/benjamin')
elif age < 16:
    print('Minime')
elif age < 18:
    print('Cadette/cadet')
elif age < 20:
    print('Junior')
elif age < 40:
    print('Sénior')
elif age > 40:
    print('Vétérane/vétéran')