from flask import Flask
from Sektioner.info import info_bp
from Sektioner.sensors import sensors_bp


app = Flask(__name__)
app.config.from_object('config.ConfigDebug')


app.register_blueprint(info_bp)
app.register_blueprint(sensors_bp)

if __name__  == "__main__":
    app.run(debug=True)