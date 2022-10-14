#Exo 1

#Correction 

text = "Iholflwdwlrq#yrxv#dyh}#uhxvvl#d#ghfu|swhu#fh#phvvdjh#$#Pdlqwhqdqw#yrxv#srxyh}#sdvvhu#d#o*h{huflfh#vxlydqw1"
key = 3
decryptedtext = ""
for i in range(len(text)):
    decryptedtext += (chr(ord(text[i]) - key))
print(decryptedtext)

#Exo 2 

x = input('Entrez un mot :')
y = []
for i in range(len(x)):
    if ord(x[i]) > 127:
        z = (hex(ord(x[i])))
        y.append(z[2:])
print(y)