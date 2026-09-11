print(__name__)

dico = {'Razvan BIZOI': {'age': 61, 'taille': 1.81},
        'Pierre FABER': {'age': 67, 'taille': 1.9},
        'Isabelle BIZOÏ': {'age': 50, 'taille': 1.65}}


def remplissage(dico:dict):
    while True:
        nom = input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        age = int(input("Entrez l'âge (nombre entier !) : "))
        taille = float(input("Entrez la taille (en mètres) : "))
        dico[nom] = {'age': age, 'taille': taille}


def enregistrement(dico:dict):
    fich = input("Entrez le nom du fichier de sauvegarde : ")
    with open(fich, "w") as ofi:
        # écriture d'une ligne-repère pour identifier le type de fichier :
        ofi.write("Dictionnaire Atelier 5.4.1\n")
        # parcours du dictionnaire entier, converti au préalable en une liste :
        for cle, valeur in list(dico.items()):
            # utilisation du formatage des chaînes pour créer l'enregistrement :
            ofi.write(f"\'{cle}\',{valeur}\n")


def lectureFichier(dico:dict):
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
        while True:
            ligne = ofi.readline()
            if ligne == '':  # détection de la fin de fichier
                break
            cle, valeur = eval(ligne)
            dico[cle] = valeur  # reconstitution du dictionnaire


def sortie(dico:dict):
    print("*** Job terminé ***")
    return 1  # afin de provoquer la sortie de la boucle


def autre(dico:dict):
    print("Veuillez frapper R, A, C, S ou T, svp.")


if __name__ == '__main__':
    # print(__name__)
    affichage(dico)