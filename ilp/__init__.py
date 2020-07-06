from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = '7dca0e88733cd8de2233d9759a36fa24'
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

from ilp import routes