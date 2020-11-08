from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all() # NEW
    return render_template("tags/index.html", tags = tags)

# @tags_blueprint.route("/tags/<id>")
# def show(id):
#     tag = tag_repository.select(id)
#     merchants = tag_repository.users(tag)
#     return render_template("tags/show.html", tag=tag, merchants=merchants)
