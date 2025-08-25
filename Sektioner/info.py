from flask import Blueprint, render_template


info_bp = Blueprint("info", __name__)


@info_bp.route("/")
def visa_info():
    return render_template("index.html")
