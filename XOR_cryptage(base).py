# demande de la clef de chiffrement
clef=raw_input("Entrez la clef de chiffrement\n")
# lecture du fichier messageclair.txt
fichier=open("messageclair.txt","r")
texteclair=fichier.read()
fichier.close()
# initialisation du texte chiffre
textechiffre=""
# chiffrement selon l'algorithme du XOR
for i in range (0,len(texteclair)):
    if 97<=ord(texteclair[i])<=122:
        caractere=texteclair[i]
        code=ord(caractere)-97
        decalage=ord(clef[i%len(clef)])-97
        codechiffre=(code+decalage)%26
        caracterechiffre=chr(codechiffre+97)
        textechiffre=textechiffre+caracterechiffre
    else:
        textechiffre=textechiffre+""
# ecriture dans le fichier messagechiffre.txt
fichier=open("messagechiffre.txt","w")
fichier.write(textechiffre)
fichier.close()