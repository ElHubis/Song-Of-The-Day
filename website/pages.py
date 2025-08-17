from flask import Blueprint, render_template
# python  -m flask --app website run --debug
from website.script import track_name, track_cover

bp = Blueprint("pages", __name__)

@bp.route("/")
def base():
    return render_template("base.html", album = track_name, cover = track_cover)