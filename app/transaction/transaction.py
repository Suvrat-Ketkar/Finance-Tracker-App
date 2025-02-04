from flask import Flask,session, render_template, Blueprint, request, redirect, url_for, jsonify
from app.authentication.auth import login_required
from app.extensions import db
from app.transaction.transaction_model import Transaction  # Assuming Transaction model exists

transaction_bp = Blueprint('trans', __name__)

@transaction_bp.route('/add-transaction', methods=['GET', 'POST'])
@login_required
def add_transaction_page():
    if request.method == 'POST':
        # Process the submitted form data
        data = request.get_json()  # For form data
        amount = float(data.get('amount'))
        category = data.get('category')
        description = data.get('description')
        transaction_date = data.get('transaction_date')  # May be empty
        
        if not transaction_date:
            from datetime import datetime
            transaction_date = datetime.now().date()  # Default to today's date

        # Save the transaction in the database
        transaction = Transaction(
            username =session['username'],  # Assuming session stores user_id
            amount=amount,
            category=category,
            description=description,
            transaction_date=transaction_date,
        )
        db.session.add(transaction)
        db.session.commit()

        # Give a confirmation or list page
        return jsonify({'message': 'Transaction added successfully'}), 201  

    # If GET request, display the form
    print(session['username'])
    # return render_template('AddTransaction.html'),200
    return render_template('InsertTransaction.html'),200

@transaction_bp.route('/api/get-transactions', methods=['GET'])
@login_required
def get_transations():
    if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
        return jsonify({"error": "Forbidden. This endpoint is not directly accessible."}), 403

    user = session['username']
    transactions = Transaction.get_user_transactions(user)
    transactions_list = [{
        'id': transaction.id,
        'username': transaction.username,
        'amount': transaction.amount,
        'category': transaction.category,
        'description': transaction.description,
        'transaction_date': transaction.transaction_date.strftime('%d-%m-%Y'),  # Format date
    } for transaction in transactions]    
    return jsonify({'transactions': transactions_list}), 200


@transaction_bp.route('/view-transactions', methods=['GET'])
@login_required
def view_transation_page():
    return render_template('ViewTransactions.html'),200




# @transaction_bp.route('/transactions')
# @login_required
# def transaction_list_page():
#     # Example route to list transactions
#     transactions = Transaction.query.filter_by(user_id=session['user_id']).all()
#     return render_template('TransactionList.html', transactions=transactions)
# @transaction_bp.route('/view-transactions', methods=['GET'])
# @login_required
# def view_transactions_page():
#     user = session['username']
#     transactions = Transaction.get_user_transactions(user)
#     transactions_list = [{
#         'id': transaction.id,
#         'username': transaction.username,
#         'amount': transaction.amount,
#         'category': transaction.category,
#         'description': transaction.description,
#         'transaction_date': transaction.transaction_date.strftime('%d-%m-%Y'),
#     } for transaction in transactions]

#     # Pass the transactions directly to the template
#     return render_template('ViewTransactions.html', transactions=transactions_list)