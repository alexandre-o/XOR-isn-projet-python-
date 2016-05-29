alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print ("\n\n\nQue voulez-vous faire?")
print ("	Option 1:crypter un document")
print ("	Option 2:decrypter un document")
choix=input("faite un choix (tapez 1 ou 2): ")
cle=input("Clé utilisée ? (en majuscules) ")

code=[0]*len(cle)#crée une liste de zero de la longeur de la cle
code[:]=cle[:] #la clé correspond aux premiers changements de lettres,[:] permet de selectionner l'ensemble de la liste
for loop in range(len(alphabet)): #loop prend la valeur de 0 jusqua loop= 25 (compteur)
    if not(alphabet[loop] in code): #si une lettre de alphabet n'est pas dans code alors 
        code.append(alphabet[loop]) #on complète le code avec les lettres non utilisées
                    
print("Entrez le nom du fichier , ou le chemin: ")
nom=input()+".txt"
fichier=open(nom,"r") #on ouvre le fichier à crypter ou décrypter en mode lecture
texte=fichier.read() #on copie le texte dans la variable texte
texte=texte.upper() #on passe tout le texte en majuscules
fichier.close() #on ferme le fichier, il n'est plus utile maintenant que le contenu est stocké dans 'texte'

if choix=="1":
    print("Choisir nom de sauvegarde : ")
    nom=input()+".txt"
    newtexte=open(nom,"w") #on ouvre un nouveau fichier txt en mode écriture
    new=[] #liste utilisée pour stocker le message entier
    mot=[] #liste provisoire permettant la formation des mots
    for i in range(len(texte)):#compteur
        if texte[i]!=" ": #si le caractère n'est pas un espace
            if texte[i] in alphabet: #si le caractère est une lettre de l'alphabet
                pos=alphabet.index(texte[i]) #on lui associe sa lettre codée
                mot.append(code[pos])  #ajout a mot la position de chaque lettre de code
            if texte[i] in ["0","1","2","3","4","5","6","7","8","9",'"',":",";",".",",","(",")","'"]: #si le caractère est un chiffre ou de la ponctuation
                mot.append(texte[i]) #le caractère est inchangé
        if texte[i]==" " or i==(len(texte)-1): #si le caratère est un espace ou si on arrive au bout du texte
            mot=''.join(x for x in mot if x) #on regroupe les éléments de la liste mot en une chaine de caractères correspondant justement à un mot
            new.append(mot) #on ajoute le mot à la liste new
            mot=[] #on commence un nouveau mot
    new=' '.join(x for x in new if x) #on regroupe tous les éléments de la liste (soit tous les mots) en une chaîne de caractères correspondant alors au texte codé
    newtexte.write(new) #on écrit ce message dans le fichier txt qu'on avait ouvert
    newtexte.close() #on ferme le fichier
    print("Cryptage terminé !!")
  
if choix=="2":
    print("Choisir nom de sauvegarde : ")
    nom=input()+".txt"
    newtexte=open(nom,"w") #on ouvre un nouveau fichier txt en mode écriture
    new=[] #liste utilisée pour stocker le message entier
    mot=[] #liste provisoire permettant la formation des mots
    for i in range(len(texte)):
        if texte[i]!=" ": #si le caractère n'est pas un espace
            if texte[i] in code: #si le caractère est une lettre de l'alphabet codé
                pos=code.index(texte[i]) #on lui associe sa lettre décodée
                mot.append(alphabet[pos])#ajout a mot la position de chaque lettre de code
            if texte[i] in ["0","1","2","3","4","5","6","7","8","9",'"',":",";",".",",","(",")","'"]: #si le caractère est un chiffre ou de la ponctuation
                mot.append(texte[i]) #le caractère est inchangé
        if texte[i]==" " or i==(len(texte)-1): #si le caractère est un espace ou si on arrive au bout du texte
            mot=''.join(x for x in mot if x) #on regroupe les éléments de la liste mot en une chaine de caractères correspondant justement à un mot
            new.append(mot) #on ajoute le mot à la liste new
            mot=[] #on commence un nouveau mot
    new=' '.join(x for x in new if x)#on regroupe tous les éléments de la liste (soit tous les mots) en une chaîne de caractères correspondant alors au texte codé
    newtexte.write(new) #on regroupe tous les éléments de la liste (soit tous les mots) en une chaîne de caractères correspondant alors au texte décodé
    newtexte.close() #on ferme le fichier
    print("Décryptage terminé !!")  

            
