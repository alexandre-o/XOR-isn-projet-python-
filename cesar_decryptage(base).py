message_decrypter=input("Votre message a decrypter:")
cle=int(input("Nombre de decalage ?:"))

longueur=len(message_decrypter)
i=0
alph=""
resultat=""
for i in range(longueur):
    asc=ord(message_decrypter[i])
    if asc>=65 or asc<=90:
        asc=asc-cle
    resultat=resultat+chr(asc)
print (resultat)