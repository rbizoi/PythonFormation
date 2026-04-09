# Formation Python 

<img src="https://github.com/rbizoi/PythonFormationCESI/blob/main/images/python-image-logo-940x530.jpeg" width="512">

# Installation 
https://www.anaconda.com/download

```
conda activate root
conda update --all
python -m pip install --upgrade pip
```
<div style='padding:15px;color:#030aa7;font-size:100%;text-align: left;font-family: Georgia, serif'>Création de l’environnement <b>cours</b> </div>
<div style='padding:15px;color:#030aa7;font-size:100%;text-align: left;font-family: Georgia, serif'><b>Windows</b> </div>

```
# conda remove -n cours --all -y
conda create -n cours -c conda-forge  python==3.12 ipython ipython-sql jupyter notebook numpy pandas pyarrow matplotlib seaborn portpicker biopython flatbuffers redis colour pydot pygraphviz pyyaml pyspark folium scikit-image scikit-learn yellowbrick lightgbm xgboost catboost plotly imgaug tifffile imagecodecs optuna kneed imbalanced-learn

conda activate cours
```

<div style='padding:15px;color:#030aa7;font-size:100%;text-align: left;font-family: Georgia, serif'><b>Linux</b> </div>

```
# conda remove -n cours --all -y
conda create -p /home/utilisateur/anaconda3/envs/cours -c conda-forge  python==3.12 ipython ipython-sql jupyter notebook numpy pandas pyarrow matplotlib seaborn portpicker biopython flatbuffers redis colour pydot pygraphviz pyyaml pyspark folium scikit-image scikit-learn yellowbrick lightgbm xgboost catboost plotly imgaug tifffile imagecodecs optuna kneed imbalanced-learn

conda activate cours
```





