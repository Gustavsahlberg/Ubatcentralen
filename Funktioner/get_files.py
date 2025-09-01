from Funktioner.Movement.load_reports import loadReports
from pathlib import Path


folder = Path("Movementreports")


print("Nu körs den här filen")
load = loadReports(folder)
load.read_files()





class gather():
    
    def get_sn():
        return set(load.get_sub_sn())
