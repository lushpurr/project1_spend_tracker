from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

#INDEX
# GET /transactions
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all() # NEW
    tags = tag_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions, tags=tags)

# NEW
# GET '/transactions/new'
@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_task():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", merchants = merchants, tags = tags)

# # CREATE
# POST '/transactions'
@transactions_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    amount = request.form["amount"]
    merchant_id = request.form["merchant_id"]
    merchant = merchant_repository.select(merchant_id)
    tag_id = request.form["tag_id"]
    tag = tag_repository.select(tag_id)
    new_transaction = Transaction(amount, merchant, tag)
    transaction_repository.save(new_transaction)
    return redirect("/transactions")

#SHOW
# GET '/transactions/<id>'

@transactions_blueprint.route("/transactions/<id>", methods=["GET"])
def show_transaction(id):
    tags = tag_repository.select(id)
    transactions = transaction_repository.select(id)
    return render_template("transactions/show.html", tags=tags, transactions=transactions)




# # EDIT
@transactions_blueprint.route("/transactions/<id>/edit", methods=["POST"])
def edit_transaction(id):
    transaction = transaction_repository.select(id)

    merchants = merchant_repository.select_all()

    tags = tag_repository.select_all()

    return render_template('transactions/edit.html', transaction=transaction, merchants=merchants, tags=tags)


# # UPDATE
@transactions_blueprint.route("/transactions/<id>", methods=["POST"])
def update_transaction(id):
    amount = request.form["amount"]

    merchant_id = request.form["merchant_id"]
    merchant = merchant_repository.select(merchant_id)

    tag_id = request.form["tag_id"]
    tag = tag_repository.select(tag_id)

    transaction = Transaction(amount, merchant, tag, id)
    transaction_repository.update(transaction)
    return redirect("/transactions")


# DELETE '/transactions/<id>'
@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_task(id):
    transaction_repository.delete(id)
    return redirect('/transactions')