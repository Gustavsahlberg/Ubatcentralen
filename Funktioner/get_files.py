from Funktioner.Movement.load_reports import loadReports
from pathlib import Path




class dataLoading():
    def __init__(self,folder_path: str):
        folder = Path(folder_path)
        print("Nu körs den här filen")
        self.load = loadReports(folder)
        self.load.read_files()
        self.crash_dict = self.load.get_crash_log()


class gather():
    data = None
    def __init__(self,folder: str = "Movementreports"):
        if gather.data is None:
            gather.data = dataLoading(folder)
        self.data = gather.data

    def get_sn(self):
        return set(self.data.load.get_sub_sn())

    def get_log(self,sn: str):
        if sn in self.data.crash_dict:
            return self.data.crash_dict[sn]

    def get_clerance(self,sn: str):
        up, down ,forward = (True,True,True)
        horizontal, vertical, log = self.data.load.get_loc()
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



    def min_max(self):
        log = self.data.load.get_pos_log()
        max_up = max(log,key=lambda name: log[name][0])
        min_up = min(log,key=lambda name: log[name][0])

        max_forward = max(log,key=lambda name: log[name][1])
        min_forward = min(log,key=lambda name: log[name][1])
        
        min_max_list = []
        for x in [max_up,min_up,max_forward,min_forward]:
            min_max_list.append([x,log[x]])

        return min_max_list