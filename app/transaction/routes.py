from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import Transaction, Products 

trans = Blueprint('trans', __name__)

@trans.route('/new_transaction', methods=['GET', 'POST'])
def new_transaction():
    if request.method == 'POST':
      product = request.form['title_product']
      count = request.form['count_product']
      user_id = session.get('userId')

      carbon_ratio = float(count) * float(Products.query.filter_by(product=product).first().ratio)

      new_transaction = Transaction(product=product, quantity=count, carbon_ratio=carbon_ratio, user_id=user_id)

      db.session.add(new_transaction)
      db.session.commit()

      return redirect(url_for('trans.newtransaction'))

    return render_template('transaction.html')