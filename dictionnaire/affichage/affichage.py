print(__name__)

def affichage(dico:dict):
    for nom in dico:
        print(f"Nom : {nom} - âge : {dico[nom]['age']:02d} ans - taille : {dico[nom]['taille']:02.2f} m.")
        #print("Nom : {0} - âge : {1} ans - taille : {2} m.".format(nom, dico[nom]['age'], dico[nom]['taille']))


def consultation(dico:dict):
    while True:
        nom = input("Entrez le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        if nom in dico:  # le nom est-il répertorié ?
            item = dico[nom]  # consultation proprement dite
            print(f"Nom : {nom} - âge : {dico[nom]['age']:02d} ans - taille : {dico[nom]['taille']:02.2f} m.")
        else:
            print("*** nom inconnu ! ***")



if __name__ == '__main__':
    # print(__name__)
    affichage(dico)