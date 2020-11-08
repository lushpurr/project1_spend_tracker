from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@locations_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all() # NEW
    return render_template("merchants/index.html", merchants = merchants)

@merchants_blueprint.route("/merchants/<id>")
def show(id):
    merchant = merchant_repository.select(id)
    tags = merchant_repository.users(merchant)
    return render_template("merchants/show.html", merchant=merchant, tags=tags)
