from flask import Blueprint, render_template
# python  -m flask --app website run --debug
from website.script import album_name, album_cover

bp = Blueprint("pages", __name__)

@bp.route("/")
def base():
    return render_template("base.html", album = album_name, cover = album_cover)