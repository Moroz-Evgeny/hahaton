from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import User

prof = Blueprint('prof', __name__)
@prof.route('/profile')
def profile():
  if 'userLogged' in session:
    userLogin = User.query.filter_by(email=session['userEmail']).first()

    return render_template('profile.html', userLogin=userLogin.login, userEmail=session['userEmail'], userId=session['userId'], userPhoto=userLogin.photo)
  
  flash('Войдите или зарегистрируйтесь', 'warning')
  return redirect(url_for('main.register'))