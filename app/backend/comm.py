import os
import predict
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file

F_UP_F='../predict' # Form upload folder
I_UP_F='../img_data'
SERVER_DATABASE='../forms' # Form Download Folder
UPLOAD_FOLDER = './../uploads'
PHOTO_FOLDER = './../img_data'

def upload_form(dat):
    print("uploading")
    f = request.files['file']
    f.save(os.path.join(UPLOAD_FOLDER, 'predict.txt'))
    p = predict.get_file(os.path.join(UPLOAD_FOLDER,'predict.txt'))
    return predict.predict(p)

def download(dat):
    path = os.path.join(SERVER_DATABASE, 'form.txt')
    return send_file(path, as_attachment=True)

def upload_photo(photo):
    f = request.files['file']
    f.save(os.path.join(PHOTO_FOLDER, photo+'.png'))
    return "Successful Upload" 

def upload_photo2(photo):
  if request.method == 'POST':
        # check if the post request has the file part
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
      file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filenam
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config[PHOTO_FOLDER], filename))
    return photo
if __name__ == "__main__":
  print(predict.get_file('../tests/form_FULL.txt'))
  print(UPLOAD_FOLDER)
