from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from app.models import User, Products
from app import db
from app.translit import transliterate

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def register():
    # for i in  open("C:/Users/ROG/Downloads/Telegram Desktop/carbon_step.csv"):
    #     product = [j for j in i.split(';')][0]
    #     ratio = float([j.replace('\n', '').replace(',', '.') for j in i.split(';')][1])
    #     new = Products(product=product, ratio=ratio)

    #     db.session.add(new)
    # db.session.commit()
    
    if request.method == 'POST':
        login = request.form['log']
        email = request.form['email_']
        password = request.form['pass']

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Пользователь с таким email уже зарегистрован', 'warning')
            return redirect(url_for('main.register'))
        
        new_user = User(login=login, email=email, password=password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.login'))
    
    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email_log']
        password = request.form['pass_log']

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session['userLogged'] = True
            session['userName'] = transliterate(user.login)
            session['userId'] = user.id

            return redirect(url_for('ind.index', userName=session['userName'], userId=session['userId']))
        else:
            flash('Сначала зарегистрируйтесь', 'warning')
            return redirect(url_for('main.register'))
        
    return render_template('login.html')


@main.route('/logout')
def logout():
    session.clear()
    session['userLogged'] = False
    return redirect(url_for('main.login'))
    


