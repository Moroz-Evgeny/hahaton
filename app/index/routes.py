from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import User, Transaction

ind = Blueprint('ind', __name__)

@ind.route('/main')
def index():
    if 'userLogged' in session:
        user_ratio = Transaction.query.filter_by(user_id=session['userId']).all()
        date = [str(i.date).split(' ')[0].split('-')[2] + '.' + str(i.date).split(' ')[0].split('-')[1] for i in user_ratio]
        ratio = [i.carbon_ratio for i in user_ratio]

        print(date, ratio)
        return render_template('index.html', date=date, ratio=ratio)
    else:
        flash('Войдите или зарегистрируйтесь', 'warning')
        return redirect(url_for('main.register'))