from flask import render_template, url_for, request, Blueprint
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from project.core.forms import LoginForm
from project.models import User

core = Blueprint('core',__name__)

@core.route('/login', methods=['GET','POST'])
def login():
    
    form=LoginForm()
    user_name = form.user_name.data
    
    if user_name is not None:
        user = User.get(user_name)

#    print(user.user_name, user_name, form.validate_on_submit())
#    print(current_user.is_authenticated)
 
    if form.validate_on_submit():
        user_name = form.user_name.data
        if user is not None:
            if user.check_password(form.password.data):
                login_user(user)
                next = request.args.get('next')
                
                if next == None or not next[0]=='/':
                    next = url_for('ui.browse')
#                print(current_user.is_authenticated)
                return redirect(next)
            else:
                flash('Incorrect Password!')
    print(current_user.is_authenticated)
    return render_template('index.html',form=form)

@core.route('/about')
def info():
    return render_template('about.html')
