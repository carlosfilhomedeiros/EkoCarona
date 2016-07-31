
from flask import Flask
from flask import render_template
from flask import request
import json
from forms import AddCaronaForm
from dbhelper import DBHelper

DB = DBHelper()

app = Flask(__name__)
app.secret_key = 's3cr3t'


@app.route('/')
def home():
    passageiros = DB.get_caroneiros()
    return render_template("home.html", items=passageiros)


@app.route('/addsearch')
def addsearch():
    return render_template("addsearch.html")


@app.route('/add')
def add():
    form = AddCaronaForm()
    return render_template("add2.html", form=form)


@app.route('/search')
def search():
    try:
        caronas = DB.get_caroneiros()
        print(caronas)
        caronas = json.dumps(caronas)
        print(caronas)
        print(caronas)
    except Exception as e:
        print(e)
        caronas = None
    return render_template("home.html", caronas=caronas)


@app.route('/submitcarona', methods=['POST'])
def add_carona():
    # Coordenadas local de saida/chegada
    saida_latitude = request.form.get('saida_latitude')
    saida_longitude = request.form.get('saida_longitude')
    chegada_latitude = request.form.get('chegada_latitude')
    chegada_longitude = request.form.get('chegada_longitude')

    departure_date = request.form.get('departure_date')
    description = request.form.get('description')
    DB.add_carona(saida_latitude, saida_longitude,
                  chegada_latitude, chegada_longitude,
                  departure_date, description)
    return home()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # , port=5000, debug=True))
