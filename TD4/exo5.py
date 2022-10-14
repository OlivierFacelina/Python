# day = int(input('Entrez le jour :'))
# month = int(input('Entrez le mois :'))
# year = int(input('Entrez l année :'))
# maxday = 30
# maxday2 = 31
# maxday3 = 29
# maxday4 = 28

# # Cas de figure où date est pas valable 
# if day > 31 or month > 12 or year < 1900 or year > 2050:
#     print('Date invalide')

# # Ici, si le mois est égal à ces chiffres, alors le maximum de jour est 30
# if (month == 4 or month == 6 or month == 9 or month == 11) and day <= maxday:
#     print(day)
# # Ici, le maximum de jour est 31
# elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= maxday2:
#     print(day)
# else:
#     print('Erreur')
    
# # Tester si une année est bisextile ou pas
# if month == 2 and (year%4==0 and year%100!=0 or year%400==0) and day <= maxday3:
#     print('Ok')
# elif month == 2 and (year%4!=0 or year%100==0 or year%400!=0) and day <= maxday4:
#     print('Test')
# else: print('Erreur')

# Correction

day = int(input('Jour'))
month = int(input('Mois'))
year = int(input('Année'))
if year >= 1900 or year <= 2050:
    if month == (1,3,5,7,8,10,12) and day <= 31:
        print('Date bonne')
    elif month == (4,6,9,11) and day <= 30:
        print('Date bonne')
    else:
        if ((year%400==0) or (year%100!=0) and (year%4==0)) and month ==2 and day <= 29:
            print('Date bonne')
        elif month == 2 and day <= 28:
            print('Date bonne')
        else: 
            print('Date pas bonne')
else: print('Date pas bonne')

