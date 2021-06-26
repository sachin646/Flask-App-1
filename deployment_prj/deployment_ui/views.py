import os
import subprocess
from flask import render_template,Blueprint, send_file
from flask_login import login_required, current_user


deployment_ui = Blueprint('deployment_ui',__name__)

@deployment_ui.route('/', defaults={'base_path': ''})
@deployment_ui.route('/<path:base_path>')
@login_required
def browse(base_path):
    # Set Home Directory
    HOME_DIR = '/home/sachin/Flask'

    # Get full path
    full_path = os.path.join(HOME_DIR, base_path)

    # Return 404.html if path doesn't exist
    if not os.path.exists(full_path):
        return render_template('error_pages/404.html')

    # send file
    if os.path.isfile(full_path):
        return send_file(full_path)

    # return file list
    file_list = os.listdir(full_path)
    return render_template('browse.html', file_list=file_list)

@deployment_ui.route('/', defaults={'base_path': ''})
@deployment_ui.route('/<path:base_path>/run')
def run_script(base_path):
    # Set Home Directory
    HOME_DIR = '/home/sachin/Flask'

    # Get full path
    full_path = os.path.join(HOME_DIR, base_path)

    # Return 404.html if path doesn't exist
    if not os.path.exists(full_path):
        return render_template('error_pages/404.html')

    # Run shell script
    a=subprocess.check_output('sh '+full_path, shell=True)
    success='Script Completed Successfully!!!'
    failure='Script Failed!!!'
    if not a:
        return render_template('browse.html', alert=success)
    else:
        return render_template('browse.html', alert=failure)
