:: to create an environment as part of the subdirectory
::  conda create --prefix ./envs --file requirements.txt
.\envs\Scripts\spyder

:: to create an environment from requirements.txt
::   conda create -n myenv --file requirements.txt
:: to create an environment specifying requirements inline
::   conda create -n myenv scipy pandas numpy matplotlib seaborn pymssql psycopg2
