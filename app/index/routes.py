from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import User

ind = Blueprint('ind', __name__)

@ind.route('/main')
def index():
    if session['userLogged']:
        return render_template('index.html')
    else:
        flash('Войдите или зарегистрируйтесь')
        return redirect(url_for('main.register'))