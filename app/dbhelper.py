import pymysql
from app import dbconfig


class DBHelper:

    def connect(self, database="ekocarona"):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def add_carona(self, saida_latitude, saida_longitude, chegada_latitude,
                   chegada_longitude,  date, description):
        connection = self.connect()

        try:
            query = """INSERT INTO carona(latitude, longitude, date, description)
            VALUES( % s, % s, % s, % s)"""
            with connection.cursor() as cursor:
                cursor.execute(query, (saida_latitude, saida_longitude,
                                       chegada_latitude,
                                       chegada_longitude, date, description))
            connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()

    def get_caroneiros(self):
        caroneiros = []
        nomes = ['Carlos', 'Vini', 'Elvis',
                 'Camila', 'Elizete', 'Tian', 'Matheus']
        for passageiro in range(1, 7):
            caroneiro = {
                'nome': nomes[passageiro],
                'profile_pic': 'https://i.vimeocdn.com/portrait/8186623_300x300',
                'amigos': ['Carlos', 'Elvis', 'Vinicius'],
                'saida_latitude': -5.8469758 + passageiro * 100,
                'saida_longitude': -35.2040659 + passageiro * 100,
                'chegada_latitude': -5.195062 + passageiro * 100,
                'chegada_longitude': -37.411681 + passageiro * 100,
                'data_day': '25',
                'date_month': 'Jul',
                'description': 'Contribuo com Gasolina'
            }
            caroneiros.append(caroneiro)
        return caroneiros
