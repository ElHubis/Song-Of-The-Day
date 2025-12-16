from flask import Blueprint, render_template
from website.script import track_name, track_cover

bp = Blueprint("pages", __name__)

@bp.route("/")
def base():
    return render_template("base.html", track = track_name, cover = track_cover)