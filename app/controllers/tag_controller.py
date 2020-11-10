from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

#index
@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all() 
    return render_template("tags/index.html", tags = tags)


# NEW
@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new.html")


# CREATE
@tags_blueprint.route("/tags", methods=["POST"])
def create_tag():
    category = request.form["category"]
    active = request.form["active"]
    new_tag = Tag(category, active)
    tag_repository.save(new_tag)
    return redirect("/transactions")


# EDIT
@tags_blueprint.route("/tags/<id>/edit", methods=["POST"])
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', tag=tag)

#UPDATE
@tags_blueprint.route("/tags/<id>", methods=["POST"])
def update_tag(id):
    category = request.form["category"]
    active = request.form["active"]
    tag = Tag(category, active, id)
    tag_repository.update(tag) 
    return redirect("/tags")

# DELETE '/tags/<id>'
@tags_blueprint.route("/tags/<id>/delete", methods=['POST'])
def delete_task(id):
    tag_repository.delete(id)
    return redirect('/tags')