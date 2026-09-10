
dico ={}

def affichage():
    for nom in dico:
        print("Nom : {0} - âge : {1} ans - taille : {2} m.". \
              format(nom, dico[nom][0], dico[nom][1]))


def consultation():
    while 1:
        nom = input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        if nom in dico:  # le nom est-il répertorié ?
            item = dico[nom]  # consultation proprement dite
            age, taille = item[0], item[1]
            print("Nom : {0} - âge : {1} ans - taille : {2} m.". \
                  format(nom, age, taille))
        else:
            print("*** nom inconnu ! ***")


def remplissage():
    while 1:
        nom = input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        age = int(input("Entrez l'âge (nombre entier !) : "))
        taille = float(input("Entrez la taille (en mètres) : "))
        dico[nom] = (age, taille)


def enregistrement():
    fich = input("Entrez le nom du fichier de sauvegarde : ")
    with open(fich, "w") as ofi:
        # écriture d'une ligne-repère pour identifier le type de fichier :
        ofi.write("Dictionnaire Atelier 5.4.1\n")
        # parcours du dictionnaire entier, converti au préalable en une liste :
        for cle, valeur in list(dico.items()):
            # utilisation du formatage des chaînes pour créer l'enregistrement :
            ofi.write(f"\'{cle}\',{valeur}\n")


def lectureFichier():
    from os import path
    fich = ""
    while not path.isfile(fich):
        fich = input("Entrez le nom du fichier de sauvegarde : ")

    with open(fich, "r") as ofi:
        # Vérification : le fichier est-il bien de notre type spécifique ? :
        repere = ofi.readline()
        if repere != "Dictionnaire Atelier 5.4.1\n":
            print("*** type de fichier incorrect ***")
            return
        # Lecture des lignes restantes du fichier :
        while 1:
            ligne = ofi.readline()
            if ligne == '':  # détection de la fin de fichier
                break
            cle, valeur = eval(ligne)
            age, taille = int(valeur[0]), float(valeur[1])
            dico[cle] = (age, taille)  # reconstitution du dictionnaire


def sortie():
    print("*** Job terminé ***")
    return 1  # afin de provoquer la sortie de la boucle


def autre():
    print("Veuillez frapper R, A, C, S ou T, svp.")


fonc ={"R":lectureFichier,"A":remplissage,\
       "C":consultation,"L":affichage,\
       "S":enregistrement,"T":sortie}
