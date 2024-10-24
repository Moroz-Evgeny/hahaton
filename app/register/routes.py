from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import User

reg = Blueprint('reg', __name__)

@reg.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Создание нового пользователя
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('register.html')