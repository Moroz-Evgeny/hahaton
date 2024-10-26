import os
import requests
from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import User, convert_image_to_base64
from werkzeug.utils import secure_filename

setting = Blueprint('setting', __name__)

@setting.route('/settings', methods=['GET', 'POST'])
def settings():
  if 'userLogged' in session:
    if request.method == 'POST':
      if 'photo' in request.files:

        file = request.files['photo']
        filename = secure_filename(file.filename)
        photo = os.path.join('uploads', filename)
        file.save(photo)
        conv_photo = convert_image_to_base64(photo)

        # Добавление фото в бд User
        user = User.query.get(session['userId'])
        print(photo)
        user.photo = conv_photo
        db.session.commit()
      if 'nameUser' in request.form:
        userName = request.form['nameUser']

        user = User.query.get(session['userId'])
        user.login = userName
        db.session.commit()



      return redirect(url_for('setting.settings'))


    userLogin = User.query.filter_by(email=session['userEmail']).first()

    return render_template('settings.html', userLogin=userLogin.login, userEmail=session['userEmail'], userId=session['userId'], userPhoto=userLogin.photo)

  flash('Войдите или зарегистрируйтесь', 'warning')
  return redirect(url_for('main.register'))