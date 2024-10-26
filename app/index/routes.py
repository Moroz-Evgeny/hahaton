from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import User

ind = Blueprint('ind', __name__)

@ind.route('/main-<userName>_<userId>')
def index(userName, userId):
    if session['userLogged']:
        return render_template('index.html', userName=userName, userId=userId)
    else:
        flash('Войдите или зарегистрируйтесь', 'warning')
        return redirect(url_for('main.register'))