mon_fichier = open("mdp.txt" , "r")
crypt = mon_fichier.read()
mon_fichier.close()

mon_fichier = open("encrypt.txt" , "r")
decrypt1 = mon_fichier.read()
mon_fichier.close()


def encrypt(crypt):
    number=input("donner une cle de cryptage (numero)")
    b=list(crypt)
    str(b)
    c=[ord(x)for x in(b)]
    d=[]
    for i in c:
        d.append(i+number)
    e=[chr(i) for i in (d)]
    e="".join(e)
    print ("ta cle est:", number,)
    mon_fichier = open("encrypt.txt" , "w")
    mon_fichier.write(e)
    mon_fichier.close()

def decrypt(decrypt1):
    number=input("quelle est la cle de cryptage ?")
    b=list(decrypt1)
    str(b)
    c=[ord(x)for x in(b)]
    d=[]
    for i in c:
        d.append(i-number)
    e=[chr(i) for i in (d)]
    e="".join(e)
    mon_fichier = open("decrypt.txt" , "w")
    mon_fichier.write(e)
    mon_fichier.close()


def menu():
    print ("Que veut-tu faire ??")
    print ("1 pour Encrypter un document")
    print ("2 pour Decrypter un ducoment")
    choice=input("fait ton choix:")
    if choice=="1":
        run = encrypt(crypt)
        run
        menu()
    elif choice=="2":
        derun=decrypt(decrypt1)
        derun
        menu()


menu()
