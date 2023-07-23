from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import Employee  # Employee modelini burada import edin
from app.views import *  # Tüm rotaları içeren views.py dosyasını import edin

if __name__ == '__main__':
    app.run(debug=True)
