from flask import Blueprint, render_template, session, flash, redirect, url_for


main = Blueprint('main', __name__)

@main.route('/')
def index():
    try:
        return render_template('register.html')
    except KeyError:
        return render_template('index.html')

# Обработка ошибки 403
@main.errorhandler(403)
def forbidden_error(error):
    flash('Доступ запрещён! Ошибка 403.')
    return render_template('index.html')

