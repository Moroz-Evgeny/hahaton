from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import User, Transaction
from datetime import datetime

ind = Blueprint('ind', __name__)

@ind.route('/main')
def index():
    if 'userLogged' in session:
        dat = str(datetime.now()).split(' ')[0].split('-')[::-1]
        user_ratio = Transaction.query.filter_by(user_id=session['userId']).all()
        date = [i.date for i in user_ratio]
        ratio = [i.carbon_ratio for i in user_ratio]

        filtered_date = []
        filtered_ratio = []

        for i in range(len(date)):
            if int(dat[0]) >= int(date[i].split('.')[0]) and int(dat[1]) == int(date[i].split('.')[1]):
                filtered_date.append(date[i])
                filtered_ratio.append(ratio[i])
            else:
                continue

        return render_template('index.html', date=sorted(filtered_date[::-1]), ratio=sorted(filtered_ratio[::-1]))
    else:
        flash('Войдите или зарегистрируйтесь', 'warning')
        return redirect(url_for('main.register'))