import os
from logging import DEBUG,INFO,ERROR


API_V1_STR = "/api/v1/assignments"
PROJECT_NAME = "Retail API"

# uat mysql
MYSQL_SERVER="127.0.0.1"
MYSQL_PORT="3306"
MYSQL_USER="root"
MYSQL_PWD="Sarvesh@12"
MYSQL_DB="assignment"

LOGFILE='cload.log'
LOGLEVEL=INFO

SQLALCHEMY_DATABASE_URI = (
    f"mysql://"+MYSQL_USER+":"+MYSQL_PWD+"@"+MYSQL_SERVER+":"+MYSQL_PORT+"/"+MYSQL_DB+"?charset=utf8"
)