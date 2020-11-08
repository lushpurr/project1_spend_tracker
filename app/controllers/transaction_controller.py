from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all() # NEW
    return render_template("transactions/index.html", transactions = transactions)

# NEW
# GET '/transactions/new'
@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_task():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", merchants = merchants, tags = tags)

# # CREATE
# POST '/transactions'
def create_transaction():
    merchant_id = request.form["merchant_id"]
    merchant = merchant_repository.select(merchant_id)
    amount = request.form("amount")
    tag_id = request.form["tag_id"]
    tag = tag_repository.select(tag_id)
    new_transaction = Transaction(merchant, amount, tag)
    transaction_repository.save(new_transaction)
    return redirect("/transactions")


# # DELETE
# # DELETE '/visits/<id>'
# @visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
# def delete_task(id):
#     visit_repository.delete(id)
#     return redirect('/visits')