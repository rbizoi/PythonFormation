# -*- coding:utf8 -*-
def main():
    print(__name__)

def changerRepertoire(nomRep = "./donnees"):
    from os import mkdir, chdir, getcwd,path
    if not path.isdir(nomRep):
        mkdir(nomRep)

    chdir(nomRep)
    rep_cour = getcwd()
    print(rep_cour)


if __name__ == '__main__' :
    main()
else :
    print ('autre appel')
