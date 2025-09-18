import hashlib
from datetime import date
from flask import Blueprint, render_template, request
from Funktioner.nuke_activator import NukeActivator



nuke_bp = Blueprint("Nuke", __name__)


activator = NukeActivator()

@nuke_bp.route("/nuke", methods=["GET", "POST"])
def nuke():
    result = None
    if request.method == "POST":
        submarine_id = request.form.get("submarine_id")
        secret_key = request.form.get("secret_key")
        activation_code = request.form.get("activation_code")
        
        result = activator.activate_nuke(submarine_id, secret_key, activation_code)
        
    return render_template("nuke.html", result=result)

