#!/bin/bash

if [ $USER != "spark" ]; then
        echo "Le script doit être exécuté en tant qu'utilisateur: spark"
        exit -1
fi

cd ~
mkdir -p ~/donnees
cd ~/donnees

hdfs dfs -mkdir -p donnees/meteo2024

annee=2024

for mois in `seq 1 12`
do
    fichier=`printf "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.%d%02d.csv.gz" $annee $mois`
    wget $fichier
    `printf "gunzip -d synop.%d%02d.csv.gz" $annee $mois`
    `printf "hdfs dfs -moveFromLocal synop.%d%02d.csv donnees/meteo2024" $annee $mois`
done

wget https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/postesSynop.csv
hdfs dfs -moveFromLocal postesSynop.csv donnees

cd ~
hdfs dfs -ls donnees/postesSynop.csv
hdfs dfs -ls donnees/meteo2024
