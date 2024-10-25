from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from app.models import User
from app import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        login = request.form['log']
        email = request.form['email_']
        password = request.form['pass']

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Пользователь с таким email уже зарегистрован')
        new_user = User(login=login, email=email, password=password)

        db.session.add(new_user)
        db.session.commit()
        session['userReg'] = True
        return redirect(url_for('main.register'))
    
    return render_template('register.html', userReg= 'userReg' in session)


# Обработка ошибки 403
@main.errorhandler(403)
def forbidden_error(error):
    flash('Доступ запрещён! Ошибка 403.')
    return render_template('index.html')

