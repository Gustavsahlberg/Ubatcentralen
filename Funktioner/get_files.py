from Funktioner.Movement.load_reports import loadReports
from pathlib import Path


folder = Path("Movementreports")


print("Nu körs den här filen")
load = loadReports(folder)
load.read_files()


crash_dict = load.get_crash_log()


class gather():
    
    def get_sn():
        return set(load.get_sub_sn())

    def get_log(sn):
        if sn in crash_dict:
            return crash_dict[sn]
