import requests
from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import Transaction, Products

trans = Blueprint('trans', __name__)

@trans.route('/new_transaction', methods=['GET', 'POST'])
def new_transaction():
    if request.method == 'POST':
        email = request.form['email']

        # Получаем информацию о покупателе по email
        api_url = f'http://localhost:5000/purchasers?email={email}'

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            purchaser_data = response.json()

            purchaser_id = purchaser_data['id']

            # Получаем чеки покупателя
            receipts_url = f'http://localhost:5000/purchasers/{purchaser_id}/receipts'
            receipts_response = requests.get(receipts_url)
            receipts_response.raise_for_status()
            receipts = receipts_response.json()

            total_carbon_ratio = 0

            # Обработка каждого чека
            for receipt in receipts:
                date = receipt['date']
                for item in receipt['items']:
                    product = item['name']
                    count = item['count']
                    
                    # Получаем коэффициент углерода для товара из базы данных
                    product_entry = Products.query.filter_by(product=product).first()
                    if product_entry:
                        carbon_ratio = count * product_entry.ratio
                        total_carbon_ratio += carbon_ratio
                try:
                    tr = Transaction.query.get(Transaction.query.filter_by(date=date, user_id = session['userId']).first().id)
                    if tr:
                        tr.carbon_ratio += carbon_ratio
                        db.session.commit()
                except:
                    new_transaction = Transaction(
                        carbon_ratio=total_carbon_ratio,
                        user_id=session['userId'],
                        date=date
                    )

                    db.session.add(new_transaction)
                    db.session.commit()

            flash('Транзакция успешно добавлена!', 'success')
            return redirect(url_for('trans.new_transaction'))

        except requests.exceptions.RequestException as e:
            flash(f"Ошибка при обращении к API: {e}", 'error')
            return redirect(url_for('trans.new_transaction'))

    return render_template('transaction.html')
