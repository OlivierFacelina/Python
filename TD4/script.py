# Exo 1 

hour = int(input('Heure :'))
minute = int(input('Minute :'))
seconde = int(input('Seconde :'))

if minute == 60 and hour == 23:
    hour = 0
    
if hour == 24:
    hour = 0
    minute = minute + 1
elif minute == 60:
    minute = 0
elif seconde == 60:
    seconde = 0
    minute = minute + 1

if hour < 24 and minute < 60:
    print(f'Dans une minute, il sera',hour,'heure(s)',minute,'minute',seconde)
elif hour > 24 or minute > 60 or seconde > 60:
    print('Erreur')