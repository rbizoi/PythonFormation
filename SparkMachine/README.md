`export PYSPARK_DRIVER_PYTHON=jupyter`<br>
`export PYSPARK_DRIVER_PYTHON_OPTS='notebook'`<br>
`pyspark --master spark://jupiter.olimp.fr:7077 --executor-cores 4 --executor-memory 8g`<br>

`export PYSPARK_DRIVER_PYTHON=python3`<br>
`export PYSPARK_DRIVER_PYTHON_OPTS=''`<br>

`rm charge_meteo_2024.sh`
`wget https://raw.githubusercontent.com/rbizoi/PythonFormation/refs/heads/main/SparkMachine/charge_meteo_2024.sh`

