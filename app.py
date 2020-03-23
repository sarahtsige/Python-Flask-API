from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('happiness', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db

class Region(BaseModel):
    name = CharField()



class Country(BaseModel):
    name = CharField()
    # region = CharField()
    rank = IntegerField()
    happiness_score = FloatField()
    region_id = ForeignKeyField(Region, backref='regions')


db.connect()


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_countries():
    countries = []
    for country in Country.select():
        countries.append(model_to_dict(country))
    return jsonify(countries)

@app.route('/regions/', methods = ['GET'])
@app.route('/regions/<id>', methods = ['GET'])
def get_regions(id = None):
    if id:
         return jsonify(model_to_dict(Region.get(Region.id == id)))
    regions = []
    for region in Region.select():
        regions.append(model_to_dict(region))
    return jsonify(regions)



@app.route('/country/region/<region>', methods=['GET'])
def get_country_by_region(region):
    countries = []
    for country in Country.select().where(Country.region_id == region):
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
