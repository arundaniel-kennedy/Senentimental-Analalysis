from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'new',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)

mycursor = link.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/new'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class data(db.Model):

    __tablename__ = "data"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} is {self.age}"




if __name__ == '__main__':
    app.run(debug=True)
