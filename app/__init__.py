from flask import Flask
import pymysql



app = Flask(__name__)



from app.main.indeximport main as main
app.register_blueprint(main)