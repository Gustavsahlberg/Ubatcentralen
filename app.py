from flask import Flask
from Sektioner.info import info_bp


app = Flask(__name__)
app.config.from_object('config.ConfigDebug')


app.register_blueprint(info_bp)

if __name__  == "__main__":
    app.run(debug=True)