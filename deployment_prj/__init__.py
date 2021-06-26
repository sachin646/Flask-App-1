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

from deployment_prj.core.views import core
from deployment_prj.users.views import users
from deployment_prj.deployment_ui.views import deployment_ui
from deployment_prj.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(deployment_ui)
app.register_blueprint(error_pages)

