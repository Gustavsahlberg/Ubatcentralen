from flask import Blueprint, render_template, request
from pathlib import Path
from Funktioner.sensor_analysis import SensorFileAnalyzer

sensors_bp = Blueprint('sensors', __name__, template_folder='../templates')

@sensors_bp.route("/sensorfel", methods=["GET", "POST"])
def sensor_overview():
    folder = Path("Sensordata")
    results = []

    search_sn = request.form.get("submarine_id", "").strip()

    files_to_analyze = list(folder.glob("*.txt"))
    if search_sn:
       
        files_to_analyze = [f for f in files_to_analyze if search_sn in f.stem]

    
    if not search_sn:
        files_to_analyze = files_to_analyze[:10]

    for file in files_to_analyze:
        analyzer = SensorFileAnalyzer(file)
        analyzer.analyze()
        summary = analyzer.summary()

        
        summary["most_common_count"] = summary["most_common_pattern"][1]
        results.append(summary)

    return render_template("sensors.html", results=results, search_sn=search_sn)
