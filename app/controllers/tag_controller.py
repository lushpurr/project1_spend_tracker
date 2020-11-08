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
    return render_template(tags/new.html)



# CREATE
@tags_blueprint.route("/tags", methods=["POST"])
def create_tag():
    category = request.form["category"]
    new_tag = Tag(category)
    tag_repository.save(new_tag)
    return redirect("/tags")


# # EDIT
# @humans_blueprint.route("/humans/<id>/edit")
# def edit_human(id):
#     human = human_repository.select(id)
#     return render_template('humans/edit.html', human=human)


# # UPDATE
# @humans_blueprint.route("/humans/<id>", methods=["POST"])
# def update_human(id):
#     name = request.form["name"]
#     human = Human(name, id)
#     human_repository.update(human)
#     return redirect("/humans")


# # DELETE
# @humans_blueprint.route("/humans/<id>/delete", methods=["POST"])
# def delete_human(id):
#     human_repository.delete(id)
#     return redirect("/humans")
