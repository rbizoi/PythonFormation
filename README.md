# Formation Python 

<img src="https://github.com/rbizoi/PythonFormationCESI/blob/main/images/python-image-logo-940x530.jpeg" width="512">

# Installation 
https://www.anaconda.com/download

## Windows
```
conda create -n cours python==3.10 ipython ipython-sql jupyter notebook numpy==1.23.5 pandas pyyaml==5.4.1 pyarrow scikit-image scikit-learn matplotlib seaborn tifffile portpicker biopython flatbuffers colour pydot pygraphviz imgaug tifffile imagecodecs

conda activate cours
# conda remove -n cours --all -y

#pip install SQLAlchemy==1.4.39 sql psycopg2 cx_Oracle
pip uninstall matplotlib seaborn
pip install matplotlib seaborn opencv-python-headless
```

## Linux

```
conda create -p /home/utilisateur/anaconda3/envs/cours python==3.10 ipython ipython-sql jupyter notebook numpy==1.23.5 pandas pyyaml==5.4.1 pyarrow scikit-image scikit-learn matplotlib seaborn  tifffile portpicker biopython Flask==2.0.2 Flask-Caching==1.10.1 Flask-Compress==1.10.1 flatbuffers  redis colour pydot pygraphviz pyyaml imgaug tifffile imagecodecs pyspark

conda activate cours
# conda remove -n cours --all -y

pip install SQLAlchemy==1.4.39 sql psycopg2 cx_Oracle
pip uninstall matplotlib seaborn
pip install matplotlib seaborn opencv-python-headless
```

```
# sudo apt install openjdk-8-jdk-headless
# sudo apt-get install libpq-dev python3-dev gcc
# pip install psycopg2-binary

cat << FIN_FICHIER > /etc/profile.d/java_dev.sh
#!/bin/bash
# Configuration Outils
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export JRE_HOME=\$JAVA_HOME/jre
export PATH=\$JAVA_HOME/bin:\$PATH
FIN_FICHIER
```


