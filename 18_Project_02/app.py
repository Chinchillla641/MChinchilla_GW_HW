from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
import os
from flask_heroku import Heroku
app = Flask( __name__ )
SQLALCHEMY_TRACK_MODIFICATIONS = "postgres://ceqpjjmbiuiqtz:e5a49ff044fd09cfa8ab52c1d23be60642f0aa3402b5847ab08658bc16a39a44@ec2-52-203-160-194.compute-1.amazonaws.com:5432/de8vg0eb5jkmn0"
DATABASE_URL = "postgres://ceqpjjmbiuiqtz:e5a49ff044fd09cfa8ab52c1d23be60642f0aa3402b5847ab08658bc16a39a44@ec2-52-203-160-194.compute-1.amazonaws.com:5432/de8vg0eb5jkmn0"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('DATABASE_URL')
heroku = Heroku(app)
db = SQLAlchemy(app)

class Dataentry(db.Model):
    __tablename__ = "Measels Data"
    State = db.Column(db.Character, primary_key=True)
    Counts = db.Column(db.Integer)

    def __init__ (self, mydata):
        self.mydata = mydata
        
@app.route("/submit", methods=["GET"])
def get_from_db():
    indata = Dataentry(request.form['mydata'])
    data = copy(indata. __dict__ )
    del data["_sa_instance_state"]
    try:
        db.session.add(indata)
        db.session.commit()
    except Exception as e:
        print("\n FAILED entry: {}\n".format(json.dumps(data)))
        print(e)
        sys.stdout.flush()
    return 'Success! To enter more data, <a href="{}">click here!</a>'.format(url_for("enter_data"))

@app.route("/")
def enter_data(): 
    return render_template("dataentry.html")

if __name__ == ' __main__':
    #app.debug = True
    app.run()