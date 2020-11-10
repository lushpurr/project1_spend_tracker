from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all() # INDEX
    return render_template("merchants/index.html", merchants = merchants)

# NEW
@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("merchants/new.html")

# CREATE
@merchants_blueprint.route("/merchants", methods=["POST"])
def create_merchant():
    name = request.form["name"]
    active = request.form["active"]
    new_merchant = Merchant(name, active)
    merchant_repository.save(new_merchant)
    return redirect("/transactions")

# EDIT
@merchants_blueprint.route("/merchants/<id>/edit", methods=["POST"])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant=merchant)

#UPDATE
@merchants_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["name"]
    active = 'active' in request.form
    merchant = Merchant(name, active, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")

# DELETE '/merchants/<id>'
@merchants_blueprint.route("/merchants/<id>/delete", methods=['POST'])
def delete_task(id):
    merchant_repository.delete(id)
    return redirect('/merchants')