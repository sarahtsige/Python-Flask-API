from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('happiness', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Country(BaseModel):
    name = CharField()
    region = CharField()
    rank = IntegerField()
    happiness_score = FloatField()


db.connect()


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_countries():
    countries = []
    for country in Country.select():
        countries.append(model_to_dict(country))
    return jsonify(countries)


@app.route('/country/region/<region>', methods=['GET'])
def get_country_by_region(region):
    countries = []
    for country in Country.select().where(Country.region == region):
        countries.append(model_to_dict(country))
    return jsonify(countries)


@app.route('/country/', methods=['POST'])
@app.route('/country/<id>', methods=['GET'])
def get_country(id=None):
    if id:
        return jsonify(
            model_to_dict(
                Country.get(Country.id == id)))
    if request.method == 'POST':
        new_country = dict_to_model(Country, request.get_json())
        new_country.save()
    return jsonify({"id": new_country.id, "success": True})


app.run(debug=True, port=9000)
