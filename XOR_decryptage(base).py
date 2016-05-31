# demande de la clef de dechiffrement
clef=raw_input("Entrez la clef de dechiffrement\n")
# lecture du fichier messagechiffre.txt
fichier=open("messagechiffre.txt","r")
textechiffre=fichier.read()
fichier.close()
# initialisation du texte clair
texteclair=""
# chiffrement selon l'algorithme du XOR
for i in range (0,len(textechiffre)):
    if 97<=ord(textechiffre[i])<=122:
        caractere=textechiffre[i]
        code=ord(caractere)-97
        decalage=ord(clef[i%len(clef)])-97
        codeclair=(code-decalage)%26
        caractereclair=chr(codeclair+97)
        texteclair=texteclair+caractereclair
    else:
        texteclair=texteclair+""
# ecriture dans le fichier messageclair.txt
fichier=open("messageclair.txt","w")
fichier.write(texteclair)
fichier.close()