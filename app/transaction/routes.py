import requests
from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from app import db
from app.models import Transaction, Products

trans = Blueprint('trans', __name__)

@trans.route('/new_transaction', methods=['GET', 'POST'])
def new_transaction():
    email = session['userEmail']
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

        for receipt in receipts:
            transaction_id = receipt['id']
            date = receipt['date']

            # Проверяем наличие транзакции по user_id и transaction_id
            existing_transaction = Transaction.query.filter_by(transaction_id=transaction_id, user_id=session['userId']).first()

            if existing_transaction:
                continue

            total_carbon_ratio = 0  # Сбрасываем сумму углеродного коэффициента для каждого нового чека

            for item in receipt['items']:
                product = item['name']
                count = item['count']

                # Получаем коэффициент углерода для товара из базы данных
                product_entry = Products.query.filter_by(product=product).first()
                if product_entry:
                    carbon_ratio = count * product_entry.ratio
                    total_carbon_ratio += carbon_ratio

            # Добавляем новую транзакцию для данного чека
            new_transaction = Transaction(
                carbon_ratio=total_carbon_ratio,
                user_id=session['userId'],
                date=date,
                transaction_id=transaction_id
            )
            db.session.add(new_transaction)
            db.session.commit()

        return redirect(url_for('ind.index'))

    except requests.exceptions.RequestException as e:
        return redirect(url_for('ind.index'))
