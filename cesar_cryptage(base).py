message_crypter=input("Votre message a crypter:")
cle=int(input("Nombre de decalage ?:"))

longueur=len(message_crypter)
i=0
alph=""
resultat=""
for i in range(longueur):
    asc=ord(message_crypter[i])
    if asc>=65 or asc<=90:
        asc=asc+cle
    resultat=resultat+chr(asc)
print (resultat)