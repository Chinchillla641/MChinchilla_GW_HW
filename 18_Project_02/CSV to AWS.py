# pandas and sqlalchemy
import pandas as pd
from sqlalchemy import create_engine

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()

# Set path 
# import sys
# sys.path.append('../../../../')

# Config variables
from config import remote_db_endpoint, remote_db_port
from config import remote_gwsis_dbname, remote_gwsis_dbuser, remote_gwsis_dbpwd
from config import local_db_user, local_db_pwd, local_db_endpoint, local_db_port, local_db_name

# import files
csv_file1 = "2019_measles.csv"
occurence_dta = pd.read_csv(csv_file1)

csv_file2 = "Vaccines.csv"
vaccine_dta = pd.read_csv(csv_file2)

csv_file3 = "Measels 24months-2016.csv"
vacpct_dta = pd.read_csv(csv_file3)

# Cloud MySQL Database Connection on AWS
engine = create_engine(f"postgresql://{remote_gwsis_dbuser}:{remote_gwsis_dbpwd}@{remote_db_endpoint}:{remote_db_port}/{remote_gwsis_dbname}")

# Cloud MySQL Database Connection on AWS
engine = create_engine(f"mysql://{remote_gwsis_dbuser}:{remote_gwsis_dbpwd}@{remote_db_endpoint}:{remote_db_port}/{remote_gwsis_dbname}")

