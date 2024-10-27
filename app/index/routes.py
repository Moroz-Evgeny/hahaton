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
        filtered_ratio_dict = {}

        for i in range(len(date)):
            if int(dat[0]) >= int(date[i].split('.')[0]) and int(dat[1]) == int(date[i].split('.')[1]):
                filtered_date.append(date[i].split('.')[0] + '.' + date[i].split('.')[1])
                filtered_ratio_dict[date[i].split('.')[0] + '.' + date[i].split('.')[1]] = ratio[i]
            else:
                continue
        filtered_date = sorted(filtered_date)
        for i in filtered_date:
            filtered_ratio.append(filtered_ratio_dict[i])
        return render_template('index.html', date=filtered_date, ratio=filtered_ratio)
    else:
        flash('Войдите или зарегистрируйтесь', 'warning')
        return redirect(url_for('main.register'))