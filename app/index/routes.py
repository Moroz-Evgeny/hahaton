from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import User

ind = Blueprint('ind', __name__)

@ind.route('/main-<userName>_<userId>')
def index(userName, userId):
    if session['userLogged']:
        data = {'date': '10.10.2024', 'carbon_ratio': 1.5818}
        return render_template('index.html', userName=userName, userId=userId, data=data)
    else:
        flash('Войдите или зарегистрируйтесь', 'warning')
        return redirect(url_for('main.register'))