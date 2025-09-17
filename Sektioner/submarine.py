from flask import Blueprint, render_template, request
from Funktioner.get_files import gather


submarine_bp = Blueprint("Ubåt", __name__)

g = gather()
subs = g.get_sn()


@submarine_bp.route("/sök", methods=["GET"])
def search_resultat():
    sn = request.args.get("q", "")

    if sn:
        sn = (f"{sn}.txt")
        if sn in subs:
            crash_log = g.get_log(sn)
            up, down ,forward = g.get_clerance(sn)
            url = "ubåt.html"
            sn = (sn[:11])
        else:
            crash_log, up, down, forward = (None,None,None,None)
            url = "error.html"
        return render_template(f"submarine/{url}",result=sn, sn=sn,crash_log=crash_log,up=up, down=down ,forward=forward)
    
    return render_template("submarine/search.html", result=None, sn=sn,crash_log=None,up=None, down=None ,forward=None)