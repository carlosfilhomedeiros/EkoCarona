import pymysql
import dbconfig

connection = pymysql.connect(host='localhost',
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = """CREATE DATABASE IF NOT EXISTS ekocarona"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS ekocarona.carona (
        id int NOT NULL AUTO_INCREMENT,
        saida_latitude FLOAT(10,6),
        saida_longitude FLOAT(10,6),
        chegada_latitude FLOAT(10,6),
        chegada_longitude FLOAT(10,6),
        date DATETIME,
        description VARCHAR(1000),
        updated_at TIMESTAMP,
        PRIMARY KEY (id))"""

        cursor.execute(sql)
    connection.commit()
finally:
    connection.close()
