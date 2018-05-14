from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = '*************'
app.config['MYSQL_DATABASE_PASSWORD'] = '*************'
app.config['MYSQL_DATABASE_DB'] = '*************'
app.config['MYSQL_DATABASE_HOST'] = '*************'
app.config['MYSQL_DATABASE_PORT'] = 0000
mysql.init_app(app)