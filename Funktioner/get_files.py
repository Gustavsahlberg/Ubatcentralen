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

    def get_clerance(sn):
        up, down ,forward = (True,True,True)
        horizontal, vertical, log = load.get_loc()
        if sn in log:
            yx = log[sn]
            if len(vertical[yx[0]]) > 1:
                for cordinate in vertical[yx[0]]:
                    if cordinate > yx[1]:
                        forward = False
                        break
            if len(horizontal[yx[1]]) > 1:
                for cordinate in horizontal[yx[1]]:
                    if cordinate > yx[0]:
                        up = False
                    elif cordinate < yx[0]:
                        down = False
        return up,down,forward

