from flask import Flask
from flask_mail import Mail



app = Flask(__name__, static_folder='./static')

app.secret_key = "edeacda59ac156398eb419c6b1ba496a5b8d0250cbf6f09299"

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'greengarry552021@gmail.com'
app.config['MAIL_PASSWORD'] = 'gfzmmhxqbxjtcxgh' #os.environ.get('MAIL_PASSWORD')


mail = Mail(app)

from fthird.main.routes import main
from fthird.portals.routes import portals

app.register_blueprint(main)
app.register_blueprint(portals)