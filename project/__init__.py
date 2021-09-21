from flask import Flask, render_template, request, send_file, flash, Blueprint
from flask_login import LoginManager

import os
import subprocess

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SaCh!N_P@tWa123'

# LOGIN CONFIGS
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'core.login'

from project.core.views import core
from project.users.views import users
from project.ui.views import ui
from project.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(ui)
app.register_blueprint(error_pages)

