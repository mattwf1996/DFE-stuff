from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://mattfarrow@mattsmysqlserver:5cba46bd79GO!@mattsmysqlserver.mysql.database.azure.com:3306/mydb"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
