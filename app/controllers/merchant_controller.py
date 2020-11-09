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
    new_merchant = Merchant(name)
    merchant_repository.save(new_merchant)
    return redirect("/merchants")