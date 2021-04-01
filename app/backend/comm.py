import os
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file

F_UP_F='../predict' # Form upload folder
I_UP_F='../img_data'
SERVER_DATABASE='../forms' # Form Download Folder

def upload_form(data):
    f = request.files['file']
    f.save(os.path.join(UPLOAD_FOLDER, 'predict.txt'))
    return "Upload success"

def download(data):
    path = os.path.join(SERVER_DATABASE, 'form.txt')
    return send_file(path, as_attachment=True)

def upload2():
  pass

