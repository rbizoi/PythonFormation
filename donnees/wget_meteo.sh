#!/bin/bash

repertoire=`pwd`
for annee in {1996..2024}
do
    cd $repertoire
    mkdir $annee
    cd $annee
    for mois in {1..12}
    do
        fichier=`printf "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.%d%02d.csv.gz" $annee $mois`
        wget $fichier
        `printf "gunzip -d synop.%d%02d.csv.gz" $annee $mois`
    done
done
cd $repertoire
