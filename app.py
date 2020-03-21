from flask import Flask
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = ProstgresqlDatabase('coutries', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db


class Country(BaseModel):
    country = CharField()
    region = CharField()
    rank = IntegerField()
    hapiness_score = DecimalField()
    
   


db.connect([Country])
#db.drop_tables([Country])
#db.create_tables()

#Bank(bank_name = '', city = '', state= , cert= '', acquiring_institution = '', closing_date = ()).save()
#Bank(bank_name = '', city = '', state= , cert= '', acquiring_institution = '', closing_date = ()).save()


app = Flask(__name__)


 
@app.route('/')
def index():
    return "Hello Sarah"





app.run(debug=True, port=9000)