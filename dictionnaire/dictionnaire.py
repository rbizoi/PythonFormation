from enregistrement.traitements import dico,lectureFichier,remplissage,enregistrement,sortie,autre
from affichage.affichage import consultation,affichage

print(__name__)
if __name__ == '__main__':

    fonc = {"R": lectureFichier, "A": remplissage, \
            "C": consultation, "L": affichage, \
            "S": enregistrement, "T": sortie}

    while True:
        choix = input("Choisissez :\n" + \
                      "(R)écupérer un dictionnaire préexistant sauvegardé dans un fichier\n" + \
                      "(A)jouter des données au dictionnaire courant\n" + \
                      "(C)onsulter le dictionnaire courant\n" + \
                      "(L)ister le dictionnaire courant\n" + \
                      "(S)auvegarder le dictionnaire courant dans un fichier\n" + \
                      "(T)erminer : ").upper()
        # l'instruction ci-dessous appelle une fonction différente pour chaque
        # choix, par l'intermédiaire du dictionnaire <fonc> :
        if fonc.get(choix, autre)(dico):
            break
        # note : toutes les fonctions appelées ici renvoient <None> par défaut
        # sauf la fonction sortie() qui renvoie 1 => sortie de la boucle