from flask import Blueprint, render_template, request
from Funktioner.get_files import gather


submarine_bp = Blueprint("Ubåt", __name__)

subs = gather.get_sn()


@submarine_bp.route("/sök", methods=["GET"])
def search_resultat():
    sn = request.args.get("q", "")

    if sn:
        sn = (f"{sn}.txt")
        if sn in subs:
            crash_log = gather.get_log(sn)
            url = "ubåt.html"
            sn = (sn[:11])
        else:
            url = "error.html"
        return render_template(f"submarine/{url}",result=sn, sn=sn,crash_log=crash_log)
    
    return render_template("submarine/search.html", result=None, sn=sn,crash_log=None)