from project import login_manager
from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user
from project.models import User


users = Blueprint('users',__name__)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@users.route('/account')
@login_required
def account():
    user = current_user.user_name
    return render_template('account.html', user=user)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.login"))
