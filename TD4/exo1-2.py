# Exo 1 

hour = int(input('Heure :'))
minute = int(input('Minute :'))
seconde = int(input('Seconde :'))
seconde = seconde + 1
if seconde >= 60:
    seconde = 0
    minute = minute + 1
    if minute >= 60:
        minute = 0
        hour = hour + 1
        if hour == 24:
            hour = 0
print(f'Dans une minute, il sera',hour,'heure(s)',minute,'minute',seconde)
 

