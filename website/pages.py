from flask import Blueprint, render_template
# python  -m flask --app website run --port 8000 --debug

bp = Blueprint("pages", __name__)

@bp.route("/")
def base():
    return render_template("base.html")